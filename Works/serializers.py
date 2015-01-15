from rest_framework import serializers
from .models import Work

class WorkSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Work
		fields = ('user', 'title', 'category','date','cover','archive',)
