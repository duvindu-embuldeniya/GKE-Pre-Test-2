from django.urls import path
from . views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('health/', health, name = 'health'),
    path('startup/', startup, name= 'startup'),
    path('ready/', readiness, name = 'ready'),
    path('live/', liveness, name = 'live'),
]