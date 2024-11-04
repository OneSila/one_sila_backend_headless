from typing import Optional

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from django.db.models import Q
from strawberry_django.filters import filter as strawberry_filter
from strawberry_django import filter_field as custom_filter
from strawberry import UNSET
from strawberry import LazyType as lazy
from core.managers import QuerySet


class SearchFilterMixin:

    @custom_filter
    def search(
        self,
        queryset: QuerySet,
        value: str,
        prefix: str
    ) -> tuple[QuerySet, Q]:

        if value not in (None, UNSET):
            queryset = queryset.search(value)

        return queryset, Q()


class ExcluideDemoDataFilterMixin:

    @custom_filter
    def exclude_demo_data(
        self,
        queryset: QuerySet,
        value: bool,
        prefix: str
    ) -> tuple[QuerySet, Q]:

        if value:
            from django.contrib.contenttypes.models import ContentType
            from core.models import DemoDataRelation

            supplier_content_type = ContentType.objects.get_for_model(queryset.model)
            queryset = queryset.exclude(
                id__in=DemoDataRelation.objects.filter(
                    content_type=supplier_content_type
                ).values("object_id")
            )

        return queryset, Q()



def filter(*args, lookups=True, **kwargs):
    return strawberry_filter(*args, **kwargs, lookups=lookups)
