from django.shortcuts import render

# Create your views here.

#páginas não relacionadas aos apps
def home_view(request):
    return render(request, 'home.html', {})

