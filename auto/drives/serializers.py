from rest_framework import serializers
from .models import Drive
from rest_framework.serializers import ModelSerializer


class DriveSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%m.%d %H:%M:%S")

    class Meta:
        model = Drive
        fields = '__all__'
