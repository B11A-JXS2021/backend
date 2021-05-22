from rest_framework import serializers
from .models import Drive
from rest_framework.serializers import ModelSerializer


class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = '__all__'
