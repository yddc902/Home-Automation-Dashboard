from django.contrib import admin
from .models import TempModel, WaterModel, DetectionModel

# Register your models here.
admin.site.register(TempModel)
admin.site.register(WaterModel)
admin.site.register(DetectionModel)
