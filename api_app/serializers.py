from django.contrib.auth.models import User, Group
from .models import TempModel, WaterModel, DetectionModel, MailModel, OpenModel
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
            water_level = validated_data['water_level'],
            water_detected = validated_data['water_detected'])

        new_detection.save()
        return new_detection

class mailserializer(serializers.ModelSerializer):
    class Meta:
        model = MailModel
        fields = '__all__'

    def create(self, validated_data):
        new_mail = MailModel(
            date = validated_data['date'],
            mail_detected = validated_data['detected'])

        new_mail.save()
        return new_mail

class openserializer(serializers.ModelSerializer):
    class Meta:
        model = OpenModel
        fields = '__all__'

    def create(self, validated_data):
        new_open = OpenModel(
            date = validated_data['date'],
            sensor_id = validated_data['sensor_id'],
            sensor_state = validated_data['sensor_state'])

        new_open.save()
        return new_open
