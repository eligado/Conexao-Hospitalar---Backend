from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import hospitais_list, ComentarioViewSet, comentarios_por_hospital

admin.site.site_header = 'Administração do Conexão Hospitalar'
admin.site.site_title = 'Administração do Conexão Hospitalar'
admin.site.index_title = ''

router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('hospitais/', hospitais_list, name='hospitais_list'),
    path('hospitais/<int:hospital_id>/comentarios/', comentarios_por_hospital, name='comentarios_por_hospital'),
    path('auth/', include('dj_rest_auth.urls')),  # login/logout
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # cadastro de usuário
    path('', include(router.urls)),
]
