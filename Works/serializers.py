# -*- encoding: utf-8 -*-

from .models import Work
from rest_framework import serializers

class WorkSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Work
