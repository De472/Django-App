from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def user_view(request, *args, **kkwargs):
    return render(request, 'user.html', {})
