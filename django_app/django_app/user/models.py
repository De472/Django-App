from django.db import models


# Create your models here.

#email e cpf unique garantem q a mesma pessoa n terá mais cadastros
class User(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)
    cpf = models.CharField(max_length=14, blank=False, unique=True)
    nome = models.CharField(max_length=50)
