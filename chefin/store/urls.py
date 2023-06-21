from django.urls import path
from .views import *

urlpatterns = [
    path('rolu', rolu, name='rolu'),
    path('pizza', pizza, name='pizza'),
    path('salat', salat, name='salat'),
    path('osnovni', osnovni, name='osnovni'),
]
