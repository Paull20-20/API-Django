from pyexpat import model
from turtle import title
from uuid import uuid4
from django.db import models

 
class Notas(models.Model):
    id_aluno = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    cpf = models.IntegerField()                 
    disciplina = models.CharField(max_length=255)
    nota01 = models.FloatField()
    nota02 = models.FloatField()                         
    nota03 = models.FloatField()
    nota04 = models.FloatField()
    media = models.FloatField()
    create_at = models.DateField(auto_now_add=True)






