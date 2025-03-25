from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HospitaisSerializer, ComentarioSerializer
from .models import Hospitais, Comentario

def hospitais_list(request):
    hospitais = Hospitais.objects.all().values()
    hospitais_list = list(hospitais)
    return JsonResponse(hospitais_list, safe=False)

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by('-criado_em')
    serializer_class = ComentarioSerializer

@api_view(['GET'])
def comentarios_por_hospital(request, hospital_id):
    comentarios = Comentario.objects.filter(hospital_id=hospital_id).order_by('-criado_em')
    serializer = ComentarioSerializer(comentarios, many=True)
    return Response(serializer.data)
