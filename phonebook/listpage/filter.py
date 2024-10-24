import django_filters
from .models import Person


class PersonFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Person
        fields = ["id", "full_name", "phone_number", "comment", "phone_type"]