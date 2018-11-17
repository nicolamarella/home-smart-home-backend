from django.urls import path, include
from .views import ListEvents, ListEventEntry

urlpatterns = [
     path('events/', ListEvents.as_view()),
     path('timeseries/<str:event_type>/', ListEventEntry.as_view()),
]
