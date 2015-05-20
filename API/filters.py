import django_filters
from Events.models import Event
from rest_framework import generics

class EventFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name = "user__username")
    class Meta:
        model = Event
        fields = ['user', 'date',]
        order_by = ['-date']