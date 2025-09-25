from django.utils import timezone
from .models import Evento
from .serializer import EventoSerializer


class EventoService:

    @staticmethod
    def _validar_data_evento(serializer):
        """serializer.validated_data.get('key'), só é poss[ivel de verificação após o uso do serializer.is_valid():{...}"""
        data_evento = serializer.validated_data.get('data_evento')
        if data_evento and data_evento < timezone.now():
            #se data_evento false, já vai para o return externo e não valida.
            """A comparação das datas é feita após o serializer.is_valid(), se os dados passerem na validação, é feito a checagem das datas, após o is_valid() o campo data_evento é transformado em um obj do tipo data para salvar no banco e o datatime.now() é um obj, por isso quando fazemos a comparação do data_evento com o timezone.now() é feita a compração de dois objs do mesmo tipo yyyy-mm-ddThh:mm:ss..."""
            return {'data_evento': ['A data do evento não pode ser no passado']}
        
        """esse retorno 'None' é feito para que na validação na chamada da função create/update tenha algum retorno de passar pela validação"""
        return None
                

    @staticmethod
    def get_all_eventos():
        evento = Evento.objects.all()
        serializer = EventoSerializer(evento, many=True)
        return serializer.data, None
    
    @staticmethod
    def create_evento(data):
        serializer = EventoSerializer(data=data)
        if serializer.is_valid():
            erro_data_evento = EventoService._validar_data_evento(serializer)
            if erro_data_evento:
                return None, erro_data_evento
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
    

    """viewDetail in the as.view()"""
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
            erro_data_evento = EventoService._validar_data_evento(serializer)
            if erro_data_evento:
                return None, erro_data_evento
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