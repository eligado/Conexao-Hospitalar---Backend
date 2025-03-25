from rest_framework import serializers
from .models import Hospitais, Comentario

class HospitaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitais
        fields = "__all__"

class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    hospital = serializers.StringRelatedField()

    class Meta: 
        model = Comentario 
        fields = '__all__'
