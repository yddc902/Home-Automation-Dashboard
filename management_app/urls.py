from django.urls import path
from . import endpoints

urlpatterns = [
    path('getRooms/', endpoints.getRooms, name="getRooms"),
]
