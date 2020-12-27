from django.urls import path
from django.conf.urls import url
from .views import CalendarView, event

urlpatterns = [
    url(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', event, name='event_edit'),
]