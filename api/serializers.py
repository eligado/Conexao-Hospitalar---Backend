from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Hospitais, Comentario

class HospitaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitais
        fields = "__all__"

class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)
    hospital = serializers.PrimaryKeyRelatedField(queryset=Hospitais.objects.all())

    class Meta:
        model = Comentario
        fields = ['id', 'usuario', 'hospital', 'texto', 'estrelas', 'criado_em']


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create (self, validated_data):
        """
        Usa create_user para já hashear a senha corretamente
        e retornar o User instanciado.
        """  
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )