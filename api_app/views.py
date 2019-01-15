from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DetectionModel
from .serializers import tempserializer, waterserializer, detectionserializer, mailserializer

import datetime
import json

def index(request):
    #DetectionModel.filter(date=datetime.today())
    return render(request, "index.html") #HttpResponse('Connected')
    #return HttpResponse("Connected")

@csrf_exempt
def post_temp(request):
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
            data={ #Must match model
                'date': datetime.datetime.now(),
                'room': received_data['Room'],
                'temperature_f': received_data['Temp'],
                'humidity': received_data['Humidity']
                })

        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Uploaded")
        else:
            print("Data not valid")
            return HttpResponse("Upload failed")

        return HttpResponse()
    else:
        return HttpResponse('')

@csrf_exempt
def post_water(request):
    if request.method == "POST":
        print("Connected to water view...")

        received_data = json.loads(request.body)

        serializer = waterserializer(
            data={
                'date': datetime.datetime.now(),
                'water_level': received_data['Level']
            })

        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Uploaded")
        else:
            print("Data not valid")
            return HttpResponse("Upload failed")

    return HttpResponse('')

@csrf_exempt
def post_water_detected(request):
    if request.method == "POST":
        print("New detection incoming...")

        print(request.body)
        received_data = json.loads(request.body)
        print(received_data)

        if int(received_data['Level']) > 10:
            wd = True
        else:
            wd = False

        serializer = detectionserializer(
            data = {
                'date': datetime.datetime.now(),
                'water_level': received_data['Level'],
                'water_detected': wd
            })

        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Uploaded")
        else:
            print("Data not valid")
            return HttpResponse("Upload failed")

    return HttpResponse('')

@csrf_exempt
def post_mail(request):
    if request.method == "POST":
        print("New mail incoming...")

        received_data = json.loads(request.body)

        if int(received_data['Detected']) > 0:
            md = True
        else:
            md = False

        serializer = mailserializer(
            data = {
                'date': datetime.datetime.now(),
                'detected': received_data['Detected']
            })

        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Uploaded")
        else:
            print("Data not valid")
            return HttpResponse("Upload failed")

    return HttpResponse('')
