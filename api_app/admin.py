from django.contrib import admin
from .models import TempModel, WaterModel

# Register your models here.
admin.site.register(TempModel)
admin.site.registers(WaterModel)
