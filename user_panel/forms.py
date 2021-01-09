from django.forms import ModelForm, DateInput
from .models import Event, EventUser, User
from django.db.models import Q

class EventForm(ModelForm):
  class Meta:
    model = Event
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['created_by_user'].disabled = True

class EventUserForm(ModelForm):
  class Meta:
    model = EventUser
    fields = ('event', 'user')

  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user', None)
    super(EventUserForm, self).__init__(*args, **kwargs)
    # filtrowanie eventu - user może wysyłać tylko zaproszenia, które sam utworzył
    eventUsers = list(EventUser.objects.filter(user=self.user).values_list('event_id', flat=True))
    events = Event.objects.filter(pk__in=eventUsers).filter(created_by_user_id=self.user.id)
    self.fields['event'].queryset = events

    # users_of_events = list(EventUser.objects.values_list('user_id', flat=True))
    users = User.objects.filter(~Q(username='admin'), ~Q(id=self.user.id))
    self.fields['user'].queryset = users

    self.fields['event'].required = True
    self.fields['user'].required = True