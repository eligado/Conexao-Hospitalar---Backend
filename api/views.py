from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .serializers import HospitaisSerializer
from .models import Hospitais

def hospitais_list(request):
    hospitais = Hospitais.objects.all().values()
    hospitais_list = list(hospitais)
    return JsonResponse(hospitais_list, safe=False)
