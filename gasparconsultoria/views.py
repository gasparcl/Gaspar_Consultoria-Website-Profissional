from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def laudos(request):
    return render(request, 'servicos/laudos.html')

def pericias(request):
    return render(request, 'servicos/pericias.html')

def treinamentos(request):
    return render(request, 'servicos/treinamentos.html')

def assessoria(request):
    return render(request, 'servicos/assessoria.html')

def contato(request):
    return render(request, 'contato.html')

def clientes(request):
    return render(request, 'clientes.html')

