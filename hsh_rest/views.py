import json
from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .models import Event, EventEntry
from .serializers import EventSerializer, EventEntrySerializer,\
    EventEntryReadSerializer
from pudb import set_trace
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class ListEvents(APIView):
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        event_type = request.data.get("event_type")
        try:
            event = Event.objects.get(event_type=event_type)
        except:
            event = Event()
            event.event_type = request.data.get("event_type")
            assert event.event_type is not None
            event.save()
        value = request.data.get("value")
        new_data = {
            "value": value,
            "event_type": event.pk,
        }
        serializer = EventEntrySerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)("model_updates", {
                "type": "receive.update",
                "object": serializer.data
            })
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListEventEntry(APIView):

    def get(self, request, event_type, format=None):
        entries = EventEntry.objects.filter(
            event_type__event_type=event_type).all()
        serializer = EventEntryReadSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, event_type, format=None):
        raise Exception("Operation not supported")
