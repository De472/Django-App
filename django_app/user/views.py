from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import User

# Create your views here.

#cadastro
def user_view(request):
    all_users = user_get_all()
    if request.method == 'POST':
        user_add(request)
    return render(request, 'user/add.html', {'users': all_users})

#lista
def user_list_view(request):
    all_user = user_get_all()
    return render(request, 'user/list.html', {'users': all_user})

####APIs####
def user_add(request):
    if request.method == 'POST':
        response = json.dumps([{}])
        new_user = {
            'email': request.POST['email'],
            'cpf': request.POST['cpf'],
            'nome': request.POST['nome']
        }
        user = User(email=new_user['email'], cpf=new_user['cpf'], nome=new_user['nome'])
        try:
            user.save()
            response = json.dumps([{'Adicionado com Sucesso': new_user}])
        except:
            response = json.dumps([{'Erro': 'Ao inserir no banco'}])
    return HttpResponse(response, content_type='text/json')

def user_get_all():
    all_user = User.objects.values()
    return all_user

