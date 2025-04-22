from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #Salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    #exibir todos os usuarios ja cadastrado em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados
    return render(request,'usuarios/usuarios.html', usuarios)