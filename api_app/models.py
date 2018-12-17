from django.db import models
from django.core import validators

class TempModel(models.Model):

    room_choices = (
        ('Kitchen', 'Kitchen'),
        ('LivingRoom', 'Living Room'),
        ('ManCave', 'Man Cave'),
        ('Bedroom', 'Bedroom'),
        ('SpareBedroom', 'Spare Bedroom'),
        ('Basement', 'Basement')
    )

    date = models.DateTimeField(auto_now=False)
    room = models.CharField(max_length=20, choices=room_choices)
    temperature_f = models.FloatField(max_length=5)
