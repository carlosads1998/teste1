from django.db import models
from .opcoes import SEXO_CHOICES, choices_estado

class User(models.Model):
    username= models.CharField(max_length=155, unique=True)
    password = models.CharField(max_length=50)
    email= models.EmailField(max_length=50, unique=True)
    gender = models.CharField(max_length=9, choices=SEXO_CHOICES)
    which= models.CharField(max_length=39, blank=True)
    estado= models.CharField(max_length=9, choices=choices_estado)
    
    def __str__(self):
        return self.username