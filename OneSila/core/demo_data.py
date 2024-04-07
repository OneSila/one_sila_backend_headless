import importlib

from core.exceptions import NotDemoDataGeneratorError
from core.models import DemoDataRelation
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db.models import ProtectedError
from model_bakery import baker
from faker import Faker
from random import randint
from faker.providers import DynamicProvider, BaseProvider
from core.countries import COUNTRY_CHOICES, num_countries

fake = Faker()


class VATProvider(BaseProvider):
    def vat_number(self, country_code: str) -> str:
        rand = randint(111111111, 999999999)
        return f"{country_code}{rand}"


fake.add_provider(VATProvider)


class CreatePrivateDataRelationMixin:
    @staticmethod
    def create_demo_data_relation(instance):
        multi_tenant_company = instance.multi_tenant_company
        DemoDataRelation.objects.create(content_object=instance, multi_tenant_company=multi_tenant_company)


class DemoDataRegistryMixin(CreatePrivateDataRelationMixin):
    @staticmethod
    def method_name(method):
        return method.__name__

    def register_private_app(self, method):
        method_name = self.method_name(method)

        if self.registry_private_apps.get(method_name):
            raise ValidationError(f"Method {method} is already present in the private app registry. You should pick a unique name.")

        self.registry_private_apps[method_name] = method

    def register_pubic_app(self, method):
        method_name = self.method_name(method)

        if self.registry_public_apps.get(method_name):
            raise ValidationError(f"Method {method} is already present in the public app registry. You should pick a unique name.")

        self.registry_public_apps[method_name] = method

    def load_apps(self):
        # To get the apps to register their demo-data, all we need to do is load the file.
        # upon loading, it will register and add all to the registry.
        for app in settings.INSTALLED_APPS:
            try:
                importlib.import_module(f"{app}.demo_data")
            except ModuleNotFoundError:
                # This approach will try to load demo-data from every app, but
                # this will not always be present - especially on external packages.
                pass

    def populate_db(self, *, multi_tenant_company):
        for val in self.registry_public_apps.values():
            try:
                if issubclass(val, PublicDataGenerator):
                    c = val()
                    c.generate()
                else:
                    raise NotDemoDataGeneratorError(f"{val.__name__} is not a subclass of PublicDataGenerator")
            except TypeError:
                val()

        for val in self.registry_private_apps.values():
            try:
                if issubclass(val, PrivateDataGenerator):
                    c = val(multi_tenant_company)
                    c.generate()
                else:
                    raise NotDemoDataGeneratorError(f"{val.__name__} is not a subclass of PrivateDataGenerator")
            except TypeError:
                val(multi_tenant_company)

    def run(self, *, multi_tenant_company):
        self.load_apps()
        self.populate_db(multi_tenant_company=multi_tenant_company)

    def delete_traversed_content_object(self, content_object):
        try:
            content_object.delete()
        except ProtectedError as e:
            for protected_intance in e.protected_objects:
                self.delete_traversed_content_object(protected_intance)

            self.delete_traversed_content_object(content_object)

    def delete_demo_data(self, *, multi_tenant_company):
        # we reverse the sequence, to avoid dealing with protected instances.
        for instance in multi_tenant_company.demodatarelation_set.all().reverse().iterator():
            try:
                # self.delete_traversed(instance)
                # instance.content_object.delete()
                self.delete_traversed_content_object(instance.content_object)
            except AttributeError:
                # Already deleted.
                pass
            instance.delete()


class DemoDataLibrary(DemoDataRegistryMixin):
    registry_private_apps = {}
    registry_public_apps = {}


class DemoDataGeneratorMixin:
    # field_mapper = {
    #     # 'field_name', 'function'
    # }
    # model = Model
    # count = 10

    def __init__(self):
        self.generated_instances = []

    def get_model(self):
        return self.model

    def get_count(self):
        return self.count

    def get_field_mapper(self):
        return self.field_mapper.items()

    def prep_baker_kwargs(self, seed):
        fake.seed_instance(seed)
        return {k: v() for k, v in self.get_field_mapper()}

    def create_instance(self, kwargs):
        return baker.make(self.get_model(), **kwargs)

    def generate(self):
        for i in range(self.get_count()):
            kwargs = self.prep_baker_kwargs(i)
            instance = self.create_instance(kwargs)
            self.generated_instances.append(instance)


class PrivateDataGenerator(DemoDataGeneratorMixin, CreatePrivateDataRelationMixin):
    def __init__(self, multi_tenant_company):
        super().__init__()
        self.multi_tenant_company = multi_tenant_company

    def prep_baker_kwargs(self, seed):
        kwargs = super().prep_baker_kwargs(seed)
        kwargs['multi_tenant_company'] = self.multi_tenant_company
        return kwargs

    def create_instance(self, kwargs):
        instance = super().create_instance(kwargs)
        self.create_demo_data_relation(instance)
        return instance


class PublicDataGenerator(DemoDataGeneratorMixin):
    pass
