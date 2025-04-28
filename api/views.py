# Django
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse

# Django REST Framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework_simplejwt.tokens import RefreshToken

# App interno
from .models import Hospitais, Comentario
from .serializers import HospitaisSerializer, ComentarioSerializer, RegisterSerializer

# --- Registro de Usuário (returns access+refresh tokens) ---
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # valida e cria o user (hash de senha incluso)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # gera tokens JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


# --- CRUD de Comentários (POST/PUT/DELETE só para users autenticados) ---
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by('-criado_em')
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # vincula o comentário ao usuário logado
        serializer.save(usuario=self.request.user)


# --- Listagem simples de hospitais (pode usar no Next.js) ---
@api_view(['GET'])
def hospitais_list(request):
    hospitais = Hospitais.objects.all()
    serializer = HospitaisSerializer(hospitais, many=True)
    return Response(serializer.data)


# --- List/Create Comentários de um Hospital específico ---
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def comentarios_por_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospitais, codigo=hospital_id)

    if request.method == 'GET':
        comentarios = Comentario.objects.filter(hospital=hospital)
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data.copy()
        comentario = Comentario(
            hospital=hospital,
            usuario=request.user,
            texto=data.get('texto'),
            estrelas=data.get('estrelas')
        )
        comentario.save()
        serializer = ComentarioSerializer(comentario)
        return Response(serializer.data, status=201)
