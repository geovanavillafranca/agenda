from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

# def index(request):
#     return redirect('/agenda/')



def lista_eventos(request):

    usuario = request.user

    # .all() pega todos os dados
    evento = Evento.objects.filter(usuario=usuario)

    # trocou para dados pois pega as informacoes
    dados = {'eventos': evento}

    return render(request, 'agenda.html', dados)

