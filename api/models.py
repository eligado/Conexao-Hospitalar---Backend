from django.db import models
from django.contrib.auth.models import User

class Hospitais(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    imagem = models.URLField(blank=True, null=True)
    hora_funcionamento = models.CharField(max_length=100)
    especialidades = models.TextField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitais"

class Comentario(models.Model):
    hospital = models.ForeignKey(Hospitais, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    estrelas = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.hospital.nome}'
