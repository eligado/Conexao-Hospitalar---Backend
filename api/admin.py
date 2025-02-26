from django.contrib import admin
from .models import Hospitais

class HospitaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'hora_funcionamento', 'especialidades',)
    search_fields= ('nome',)

# Register your models here.
admin.site.register(Hospitais, HospitaisAdmin)