from django.forms import ModelForm, DateInput
from .models import Event, EventUser

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

    fields = '__all__'
  def __init__(self, *args, **kwargs):
    super(EventUserForm, self).__init__(*args, **kwargs)