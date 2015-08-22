#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
import django_filters


class GenericUserFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(name="user__username", lookup_type='iexact')

    class Meta:
        fields = ['user']
        order_by = ['user']


class GenericSocialSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'user', 'profile_url', 'network_username')
