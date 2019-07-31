from django.db import models
from django.core import validators

# Create your models here.
class RoomModel(models.Model):
    room_id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    room = models.CharField(max_length=20)
    room_real_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    room_key = models.CharField(max_length=256)
