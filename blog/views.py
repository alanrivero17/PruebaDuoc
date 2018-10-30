from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def base_list(request):
    return render(request, 'blog/base.html')

def registrar_list(request):
    return render(request, 'blog/Registro.html')
def afortunado_list(request):
    return render(request, 'blog/Afortunado.html')
def marlene_list(request):
    return render(request, 'blog/Marlene.html')
def okon_list(request):
    return render(request, 'blog/Okon.html')
def atacamita_list(request):
    return render(request, 'blog/Atacamita.html')
def login_list(request):
    return render(request, 'blog/login.html')


