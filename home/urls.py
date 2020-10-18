from django.urls import path
from .views import index

urlpatterns = [
    #path('', index, name='view_news'),
    path('', index)
]