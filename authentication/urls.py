from django.urls import path
from .views import log_in, log_out, signup

urlpatterns = [
    #path('', index, name='view_news'),
    path('login', log_in),
    path('logout', log_out),
    path('signup', signup)
]