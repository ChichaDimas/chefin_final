from django.urls import path
from .views import rolu

urlpatterns = [
    path('rolu', rolu, name='rolu'),
]
