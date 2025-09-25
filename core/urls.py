from django.urls import path
from .views import EventoDetailAPIView, EventoListCreateAPIView


urlpatterns = [
    path('eventos/', EventoListCreateAPIView.as_view(), name='eventoListCreate'),
    path('eventos/<int:pk>/', EventoDetailAPIView.as_view(), name='eventoDetail')
]