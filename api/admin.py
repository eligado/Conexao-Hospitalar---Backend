from django.contrib import admin
from .models import Hospitais, Comentario

class HospitaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'hora_funcionamento', 'especialidades',)
    search_fields = ('nome',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'hospital', 'estrelas', 'criado_em')
    search_fields = ('usuario__username', 'hospital__nome')
    list_filter = ('estrelas', 'criado_em')

# Registrar os modelos no Django Admin (APENAS UMA VEZ)
admin.site.register(Hospitais, HospitaisAdmin)
admin.site.register(Comentario, ComentarioAdmin)