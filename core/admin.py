from django.contrib import admin
from core.models import Evento

# Register your models here.S


class EventoAdmin(admin.ModelAdmin):
    # quais campos quero que apareca
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',)

# essa classe Evento registra EventoAdmin
admin.site.register(Evento, EventoAdmin)
