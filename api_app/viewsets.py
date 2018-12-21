from .models import TempModel, WaterModel
from rest_framework import viewsets
from .serializers import tempserializer, waterserializer

class TempViewSet(viewsets.ModelViewSet):
        queryset = TempModel.objects.all()
        serializer_class = tempserializer

class WaterViewSet(viewsets.ModelViewSet):
    queryset = WaterModel.objects.all()
    serializer_class = waterserializer
