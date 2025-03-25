from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hospitais(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    hora_funcionamento = models.CharField(max_length=100)
    especialidades = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='hospitais', null=True, blank=True)

    class Meta:
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitais"


    def __str__(self):
        return self.nome

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey('Hospitais', on_delete=models.CASCADE)
    texto = models.TextField()
    estrelas = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario.username} para {self.hospital.nome}"