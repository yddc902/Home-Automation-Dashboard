from django.contrib.auth.models import User, Group
from .models import TempModel
from rest_framework import serializers

#Serializer to access the 'Users' database. This is Django's built in user database
class tempserializer(serializers.ModelSerializer):
    class Meta:
        model = TempModel
        fields = '__all__' #('date','room','temperature_f')

    def create(self, validated_data):
        new_temp = TempModel(
            #date = datetime.datetime.now(),
            date = validated_data['date'],
            room = validated_data['room'],
            temperature_f = validated_data['temperature_f'])

        new_temp.save()
        return new_temp
