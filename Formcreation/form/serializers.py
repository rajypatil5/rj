from rest_framework import serializers
from .models import registrationModel

class registrationSer(serializers.ModelSerializer):
    class Meta:
        model=registrationModel
        fields='__all__'