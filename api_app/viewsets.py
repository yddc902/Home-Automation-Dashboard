from .models import TempModel, WaterModel, DetectionModel, MailModel
from rest_framework import viewsets
from .serializers import tempserializer, waterserializer, detectionserializer, mailserializer

class TempViewSet(viewsets.ModelViewSet):
    queryset = TempModel.objects.all()
    serializer_class = tempserializer

class WaterViewSet(viewsets.ModelViewSet):
    queryset = WaterModel.objects.all()
    serializer_class = waterserializer

class DetectionViewSet(viewsets.ModelViewSet):
    queryset = DetectionModel.objects.all()
    serializer_class = detectionserializer

class MailViewSet(viewsets.ModelViewSet):
    queryset = MailModel.objects.all()
    serializer_class = mailserializer
