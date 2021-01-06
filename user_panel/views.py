from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta, date
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm

class CalendarView(generic.ListView):
    model = Event
    template_name = 'user_panel/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        logged_user = getLoggedUser(self.request)
        cal = Calendar(d.year, d.month, logged_user)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    instance2 = EventUser()
    eventExists = False

    if event_id:
        eventExists = True
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
        instance.created_by_user = request.user

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()

        if not eventExists:
            instance2.user = request.user
            instance2.event = instance
            instance2.save()

        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'user_panel/meet.html', {'form': form})


def getLoggedUser(request):
    return request.user

def events(request):
    eventUsers = list(EventUser.objects.filter(user=request.user).values_list('event_id', flat=True))
    events = Event.objects.filter(pk__in=eventUsers)

    # todo - zwracać do events.html eventy z przeszłości, przyszłości i aktualne (?)
    return render(request, 'user_panel/events.html', {'events': events})

def invitations(request):
    return render(request, 'user_panel/invitations.html')