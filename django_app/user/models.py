from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(null=False)
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=50)
