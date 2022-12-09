from django.shortcuts import render, redirect, HttpResponse
from .models import Usuario
from django.db.models import Q
import requests

def manager(request):
    """Lista todos os usuários cadastrados no banco de dados."""

    users = Usuario.objects.all()
    return render(request, "manage.html", {"usuarios": users})

def search(request):
    """Busca o valor do input 'pesquisar' nas colunas 'usuario' e 'nome' do database.
    Retorna os nomes e usuarios achados no banco de dados."""

    search = request.POST.get("search")
    users = Usuario.objects.filter(Q(usuario__startswith=search) | Q(nome__startswith=search))
    return render(request, "manage.html", {"usuarios": users})


def deletar(request, id):
    """Remove o usuário do banco de dados cujo 'id' informado é o mesmo no database"""

    user = Usuario.objects.get(id=id)
    user.delete()
    return redirect(manager)


def salvar(request):
    """Cria um novo usuário no banco de dados a partir do nome de usuário (username)."""

    user = request.POST.get("name")
    Usuario.objects.create(usuario=user)
    return redirect(manager)


def registrar(request):
    """Cadastra um novo usuário no banco de dados com 'nome', 'usuario', 'email' e 'senha' preenchidos.
    E faz a verificação se o mesmo usuário ou e-mail já existem no banco.
    """

    name = request.POST.get("name")
    username =request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")

    # Fazer a verificação da existencia no banco

    print(f"USUARIO CRIADO:\n{name=}\n{email=}\n{password=}\n{username=}\n")
    Usuario.objects.create(nome=name, usuario=username, email=email, senha=password)

    return render(request, "entry.html")


def entrar(request):
    """"""
    user_email = request.POST.get("user_email")
    password = request.POST.get("password")
    
    print(f"LOGIN:\n{user_email=}\n{password=}")
    # REMOVER A DUPLICATA DE USUARIOS

    bool_, mensagem = False, ""
    searchUser = lambda text_value: Usuario.objects.filter(Q(email=text_value) | Q(usuario=text_value))


    if searchUser(user_email).exists():
        if searchUser(user_email)[0].senha == password:
            return redirect(manager)

        else: bool_, mensagem = True, "Senha incorreta!"
    elif None in [user_email, password]: bool_= False
    else: bool_, mensagem = True, "E-mail ou usuário não existem!"

    return render(request, "entry.html", {"bool": bool_, "mensagem": mensagem})
    

def editar(request, id):
    """"""

    name = request.POST.get("nome")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("senha")

    user = Usuario.objects.filter(id=id).update(
        nome=name,
        usuario=username,
        email=email,
        senha=password
    )
    return redirect(manager)