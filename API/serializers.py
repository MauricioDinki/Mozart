from Events.models import Event
from rest_framework import serializers
# from Utils.mixins import UsernameSerializerMixin

class EventSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
	class Meta:
		model = Event
		fields = ('cover', 'date', 'description', 'finish_time', 'name', 'place', 'slug', 'start_time', 'user',)