from django.contrib.auth.models import User, Group
from .models import TempModel, WaterModel, DetectionModel
from rest_framework import serializers

#Serializer to access the 'Users' database. This is Django's built in user database
class tempserializer(serializers.ModelSerializer):
    class Meta:
        model = TempModel
        fields = '__all__' #('date','room','temperature_f', humidity)

    def create(self, validated_data):
        new_temp = TempModel(
            #date = datetime.datetime.now(),
            date = validated_data['date'],
            room = validated_data['room'],
            temperature_f = validated_data['temperature_f'],
            humidity = validated_data['humidity'])

        new_temp.save()
        return new_temp

class waterserializer(serializers.ModelSerializer):
    class Meta:
        model = WaterModel
        fields = '__all__' #(date, water_level)

    def create(self, validated_data):
        new_level = WaterModel(
            date = validated_data['date'],
            water_level = validated_data['water_level'])

        new_level.save()
        return new_level

class detectionserializer(serializers.ModelSerializer):
    class Meta:
        model = DetectionModel
        fields = '__all__' #(date, water_level, water_detected)

    def create(self, validated_data):
        new_detection = DetectionModel(
            date = validated_data['date'],
            water_level = validated_datap['water_level'])

        new_detection.save()
        return new_detection
