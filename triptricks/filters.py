from triptricks.models import Plan
import django_filters
from django import forms

class PlanFilter(django_filters.FilterSet):
    destination_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Plan
        fields = ['destination_name']
         
