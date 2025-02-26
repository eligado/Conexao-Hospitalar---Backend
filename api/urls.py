from django.urls import path
from django.contrib import admin
from .views import hospitais_list

admin.site.site_header = 'Administração do Conexão Hospitalar'
admin.site.site_title = 'Administração do Conexão Hospitalar'
admin.site.index_title = ''

urlpatterns = [
    path('hospitais/', hospitais_list, name='hospitais_list'),
]