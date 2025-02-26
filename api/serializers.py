from rest_framework import serializers
from .models import Hospitais

class HospitaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitais
        fields = "__all__"
