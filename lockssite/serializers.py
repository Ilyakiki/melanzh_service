import io
from rest_framework import serializers
from .models import *


# Сериализатор для модели Service
class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Service
        fields = "__all__"
