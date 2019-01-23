from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DetectionModel, TempModel, MailModel, WaterModel
from .serializers import tempserializer, waterserializer, detectionserializer, mailserializer
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


import datetime
import json

def last_temp(request,room):
    obj = TempModel.objects.filter(room__contains=room).order_by('-id')[:1]
    json_serializer = serializers.get_serializer("json")()
    data = json_serializer.serialize(obj, ensure_ascii=False)
    return HttpResponse(data)

def water_level(request):
    obj = TempModel.objects.filter(room__contains="LivingRoom").order_by('-id')[:1]
    print(obj)
    json_serializer = serializers.get_serializer("json")()
    data = json_serializer.serialize(obj, ensure_ascii=False)
    return HttpResponse(data)

def mail_delivered(request):
    obj = MailModel.objects.all().order_by('-id')[:1]
    json_serializer = serializers.get_serializer("json")()
    data = json_serializer.serialize(obj, ensure_ascii=False)
    return HttpResponse(data)

def str_test(request,room):
    return HttpResponse(room)

"""
class ListTemp(APIView):
    def get(self, request, format=None):
        temp = [TempModel.temperature_f for temp in TempModel]
"""
