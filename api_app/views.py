from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import datetime
import json

def index(request):
    return render(request, "index.html") #HttpResponse('Connected')

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

        return HttpResponse('Upload completed')

def post_water_detected(request):
    if request.method == "POST":
        print("New detection incoming...")

        received_data = json.loads(request.body)

        if received_data['Level'] > 10:
            wd = True
        else:
            wd = False

        serializer = detectionserializer(
            data = {
                'date': datetime.datetime.now(),
                'water_level': received_data['Level'],
                'water_detected': wd
            })
