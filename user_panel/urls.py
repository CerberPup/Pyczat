from django.conf.urls import url
from .views import CalendarView, event, events, invitations, event_invite

urlpatterns = [
    url(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    url(r'^events/$', events, name='events'),
    url(r'^event/new/$', event, name='event_new'),
    url(r'^event/invite/$', event_invite, name='event_invite'),
    url(r'^event/edit/(?P<event_id>\d+)/$', event, name='event_edit'),
    url(r'^invitations/$', invitations, name='invitations'),
]