# -*- encoding: utf-8 -*-

from .models import Work
from rest_framework import serializers

class WorkSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
	class Meta:
		model = Work
		fields = ('title', 'slug', 'date', 'description', 'category', 'cover', 'archive', 'work_type', 'user')
