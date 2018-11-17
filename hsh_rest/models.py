from django.db import models
from pudb import set_trace
# Create your models here.


class Event(models.Model):
    event_type = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.event_type.__str__()


class EventEntry(models.Model):
    event_type = models.ForeignKey(Event, on_delete=models.CASCADE,
                                   related_name='time_series')
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=1024)
