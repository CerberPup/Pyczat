from django.urls import path
from .views import calendar, meet

urlpatterns = [
    #path('', index, name='view_news'),
    path('calendar', calendar),
    path('meet', meet)
]