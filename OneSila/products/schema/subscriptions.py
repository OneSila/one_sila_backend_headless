from core.schema.core.subscriptions import type, subscription, Info, AsyncGenerator, model_subscriber

from products.models import Product, BundleProduct, UmbrellaProduct, SimpleProduct, ProductTranslation, \
    UmbrellaVariation, BundleVariation, ManufacturableProduct, DropshipProduct, SupplierProduct, BillOfMaterial
from products.schema.types.types import ProductType, BundleProductType, UmbrellaProductType, \
    SimpleProductType, ProductTranslationType, UmbrellaVariationType, BundleVariationType, ManufacturableProductType, DropshipProductType, \
    SupplierProductType, BillOfMaterialType


@type(name="Subscription")
class ProductsSubscription:
    @subscription
    async def product(self, info: Info, pk: str) -> AsyncGenerator[ProductType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=Product):
            yield i

    @subscription
    async def bundle_product(self, info: Info, pk: str) -> AsyncGenerator[BundleProductType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=BundleProduct):
            yield i

    @subscription
    async def umbrella_product(self, info: Info, pk: str) -> AsyncGenerator[UmbrellaProductType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=UmbrellaProduct):
            yield i

    @subscription
    async def simple_product(self, info: Info, pk: str) -> AsyncGenerator[SimpleProductType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=SimpleProduct):
            yield i

    @subscription
    async def product_translation(self, info: Info, pk: str) -> AsyncGenerator[ProductTranslationType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=ProductTranslation):
            yield i

    @subscription
    async def umbrella_variation(self, info: Info, pk: str) -> AsyncGenerator[UmbrellaVariationType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=UmbrellaVariation):
            yield i

    @subscription
    async def bundle_variation(self, info: Info, pk: str) -> AsyncGenerator[BundleVariationType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=BundleVariation):
            yield i


    @subscription
    async def manufacturable_product(self, info: Info, pk: str) -> AsyncGenerator[ManufacturableProductType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=ManufacturableProduct):
            yield i

    @subscription
    async def dropship_product(self, info: Info, pk: str) -> AsyncGenerator[DropshipProductType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=DropshipProduct):
            yield i

    @subscription
    async def supplier_product(self, info: Info, pk: str) -> AsyncGenerator[SupplierProductType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=SupplierProduct):
            yield i

    @subscription
    async def bill_of_material(self, info: Info, pk: str) -> AsyncGenerator[BillOfMaterialType, None]:
        async for i in model_subscriber(info=info, pk=pk, model=BillOfMaterial):
            yield i