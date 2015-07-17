#!/usr/bin/python
# -*- coding: utf-8 -*-

import django_filters


class GenericUserFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name="user__username", lookup_type='iexact')

    class Meta:
        fields = ['user']
        order_by = ['user']
