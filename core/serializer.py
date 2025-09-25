from rest_framework import serializers
from .models import Evento


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id','nome_evento', 'data_evento', 'local_evento', 'data_criacao']
        read_only_fields = ['id','data_criacao']