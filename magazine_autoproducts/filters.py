import django_filters
from .models import Autoproduct
from .models import Store
class AutoproductFilter(django_filters.FilterSet):
    class Meta:
        model = Autoproduct
        fields = {
            'Autoproduct_type': ['icontains'],
            'Price': ['lte', 'gte'],
            'Material': ['icontains'],
            'Color': ['icontains'],
        }


class StoreFilter(django_filters.FilterSet):
    class Meta:
        model = Store
        fields = {
            'Store_name': ['icontains'],
            'Description': ['icontains'],
        }
