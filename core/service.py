from .models import Evento
from .serializer import EventoSerializer


class ServiceEvento:

    @staticmethod
    def get_all_eventos():
        evento = Evento.objects.all()
        serializer = EventoSerializer(evento, many=True)
        return serializer.data, None
    
    @staticmethod
    def create_evento(data):
        serializer = EventoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
    

    @staticmethod
    def get_pk_evento(pk):
        try:
            evento = Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            return None, {"errors":"Evento não localizado"}
        serializer = EventoSerializer(evento)
        return serializer.data, None
    

    @staticmethod
    def update_evento(pk, data, partial=False):
        try:
            evento = Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            return None, {"error":"Evento não localizado"}
        
        serializer = EventoSerializer(instance=evento, data=data, partial = partial)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
    
    @staticmethod
    def delete_evento(pk):
        try:
            evento = Evento.objects.get(pk=pk)
            evento.delete()
            return True, None
        except Evento.DoesNotExist:
            return None, {"error":"Evento não localizado"}