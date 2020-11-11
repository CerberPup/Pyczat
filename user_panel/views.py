from django.shortcuts import render

# Create your views here.
def calendar(request):
    return render(request, 'user_panel/calendar.html')

def meet(request):
    return render(request, 'user_panel/meet.html')