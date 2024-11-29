from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.conf import settings


import re
from ecommerce.utils.validacpf import valida_cpf



class Perfil(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    
    

    def __str__(self):
        return f'{self.usuario}'

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
