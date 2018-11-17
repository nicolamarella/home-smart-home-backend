import json
from rest_framework import serializers
from .models import Event, EventEntry
from pudb import set_trace


class JSONSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        return json.dumps(data)

    def to_representation(self, obj):
        return json.loads(obj)

    def create(self, validated_data):
        raise Exception("Operation not supported")


class EventEntrySerializer(serializers.ModelSerializer):
    value = JSONSerializer()

    class Meta:
        model = EventEntry
        fields = ('timestamp', 'value', 'event_type')


class EventEntryReadSerializer(EventEntrySerializer):
    event_type = serializers.StringRelatedField()


class EventSerializer(serializers.ModelSerializer):
    # time_series = EventEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'event_type')
