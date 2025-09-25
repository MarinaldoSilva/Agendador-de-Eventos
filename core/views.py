from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .service import EventoService


class EventoListCreateAPIView(APIView):

    def get(self, request):
        eventos, errors = EventoService.get_all_eventos()
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(eventos, status=status.HTTP_200_OK)
    
    def post(self, request):
        eventos, errors = EventoService.create_evento(data=request.data)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(eventos, status=status.HTTP_201_CREATED)
    
class EventoDetailAPIView(APIView):

    def get(self, request, pk):
        eventos, errors = EventoService.get_pk_evento(pk)
        if errors:
            return Response(errors, status=status.HTTP_404_NOT_FOUND)
        return Response(eventos, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        eventos, errors = EventoService.update_evento(pk, request.data)
        if errors:
            return Response(errors, status=status.HTTP_404_NOT_FOUND)
        return Response(eventos, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        eventos, errors = EventoService.update_evento(pk, request.data, partial=True)
        if errors:
            return Response(errors, status=status.HTTP_404_NOT_FOUND)
        return Response(eventos, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        eventos, errors = EventoService.delete_evento(pk)
        if errors:
            return Response(errors, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)    
        