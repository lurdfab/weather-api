from rest_framework import serializers
from .models import *

class DescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description
        fields = ("id", "weather_description", "temperature", "created_at" )