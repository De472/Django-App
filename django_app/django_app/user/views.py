from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import  serializers
import json
from .models import User
from .forms import UserForm


# Create your views here.

def user_view(request):
    if request.method == 'POST':
        user_add(request)
    return render(request, 'user/add.html', {})

def user_list_view(request):
    user_all = user_get_all(request)
    print(user_all.serialize().decode('utf-8').split('{'))
    return render(request, 'user/list.html', {'users': User.objects.values()})

def user_search_view(request, nome):
    context = {}
    query = User.objects.filter(nome=nome)

    users = user_get_by_nome(request, 'bia')
    print(users)
    print(type(users))

    return render(request, 'user/list.html', {'users': users})
#n utilizado
def user_form_view(request):
    form = 'a'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
            form = UserForm()
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'user/add.html', context)

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

#n consegui utilizar, quando passava pro template sempre vinha ou com
#b' e/ou Content-type no começo do json (ai eu n conseguia passar pelo %for%
def user_get_all(request):
    if request.method == 'GET':
        response = list(User.objects.values())
        try:
            response = response
        except:
            response = {'Erro': 'Não deu pra pegar Get_All'}

    return JsonResponse(response,  safe=False)

def user_get_by_nome(request, nome):
    if request.method == 'GET':
        response = json.dumps([{}])
        users = User.objects.filter(nome=nome)
        print(users)
        try:
            user = User.objects.filter(nome=nome)
            response = json.dumps([{'Email': user.email, 'Cpf': user.cpf, 'Nome': user.nome}])
        except:
            response = json.dumps([{'Erro:': 'Sem registro'}])
        return HttpResponse(response, content_type='text/json')
