from Events.models import Event
from rest_framework import serializers
from Utils.mixins import UsernameSerializerMixin

# class EventSerializer(UsernameSerializerMixin, serializers.HyperlinkedModelSerializer):
class EventSerializer(serializers.HyperlinkedModelSerializer):
	# user = UsernameSerializerMixin.user
	class Meta:
		model = Event
		fields = ('cover', 'date', 'description', 'finish_time', 'name', 'place', 'slug', 'start_time', 'user',)

