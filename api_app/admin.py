from django.contrib import admin
from .models import TempModel, WaterModel, DetectionModel, MailModel

# Register your models here.
admin.site.register(TempModel)
admin.site.register(WaterModel)
admin.site.register(DetectionModel)
admin.site.register(MailModel)
