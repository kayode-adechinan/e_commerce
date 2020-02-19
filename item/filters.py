import django_filters
from item.models import Item


class ItemFilter(django_filters.FilterSet):
    class Meta:
        fields = {
            "name": ["exact", "icontains"],
            "price":["range", "lte", "gte"],
            "category":["exact"],
        }
        model = Item
