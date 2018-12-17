from django.shortcuts import render
from django.http import HttpResponse
from .models import TempModel
import datetime
import json
from rest_framework import viewsets
from .serializers import tempserializer
from django.views.decorators.csrf import csrf_exempt

def index(requst):
    return HttpResponse('Connected')

@csrf_exempt
def post(request):
    if request.method == "POST":
        print('Connected to view...')

        #print(request.POST)
        #print(request.body)

        print(datetime.datetime.now())

        received_data = json.loads(request.body)
        print(received_data)
        print(received_data['Room'])
        print(received_data['Temp'])
        print(received_data['Humidity'])

        serializer = tempserializer(
            data={
                'date': datetime.datetime.now(),
                'room': received_data['Room'],
                'temperature_f': received_data['Temp'],
                'humidity': received_data['Humidity']
                })

        if serializer.is_valid():
            #serializer.save()
            return HttpResponse("Uploaded")
        else:
            print("Data not valid")
            return HttpResponse("Upload failed")

        return HttpResponse()
    else:
        return HttpResponse('')

class TempViewSet(viewsets.ModelViewSet):
        queryset = TempModel.objects.all()
        serializer_class = tempserializer
