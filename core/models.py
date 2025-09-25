from django.db import models


class Evento(models.Model):
    nome_evento = models.CharField(max_length=255)
    data_evento = models.DateTimeField()
    local_evento = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_evento
