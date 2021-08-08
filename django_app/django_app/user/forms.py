from django import forms
from .models import User

class UserForm(forms.Form):
    email = forms.EmailField()
    cpf = forms.CharField(max_length=14)
    nome = forms.CharField(max_length=50)