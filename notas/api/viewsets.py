from rest_framework import viewsets
from notas.api import serializers
from notas import models

class NotasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NotasSerializer
    queryset = models.Notas.objects.all() #aqui nada mais é do que todos os campos do nosso modelo



    
    


