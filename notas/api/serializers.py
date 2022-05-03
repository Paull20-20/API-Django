from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from notas import models

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notas
        fields = '__all__'


        