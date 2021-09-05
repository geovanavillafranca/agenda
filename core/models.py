from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
                    # tipo do campo e seu limite
    titulo = models.CharField(max_length=100)
                        # quer dizer que pode ficar em branco e igual a nulo
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    # esse dato tem que ser automatico
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

