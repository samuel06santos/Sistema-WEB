from django.shortcuts import render, redirect, HttpResponse
from .models import Usuario
from django.db.models import Q
import requests
# import sqlite3
# import pandas as pd

def home(request):
    return render(request, "home.html", {})

def manager(request):
    """Retorna todos as informações dos usuários cadastrados no banco de dados.
    E listeia-os todos no manage.html"""

    users = Usuario.objects.all()
    return render(request, "manage.html", {"usuarios": users})

def search(request):
    """Busca o valor do input 'pesquisar' nas colunas 'usuario' e 'nome' do database.
    Retorna os nomes e usuarios achados no banco de dados."""

    search = request.POST.get("search")
    users = Usuario.objects.filter(Q(usuario__icontains=search) | Q(nome__icontains=search))
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
    """Cadastra um novo usuário no banco de dados com 'nome', 'usuario', 'email' e 'senha' preenchidos."""

    name = request.POST.get("name")
    username =request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    
    # Cria um novo usuário com o nome, usuario, email e senha passados nos campos de input's do HTML.
    Usuario.objects.create(nome=name, usuario=username, email=email, senha=password)

    users = Usuario.objects.all()
    return render(request, "entry.html", {"users": users})


def searchUser_Email(value_text, column):
    """Faz uma busca no banco de dados com a string passada no 'value_text'.\n
    Se 'column' for igual a 'usuario' realiza a busca na coluna do usuario,
    e caso seja 'email' busca na coluna do email no banco de dados.
    value_text (str): string a ser buscada
    column (str): 'usuario' | 'email'
    """
    return Usuario.objects.filter([Q(email=value_text), Q(usuario=value_text),][1 if column=="usuario" else 0 if column=="email" else 3])

# Função abandonada, não usamos mais, mas resolvemos deixá-la aí. press F to pay respect
# def searchUser(text_value):
#     return Usuario.objects.filter(Q(email=text_value) | Q(usuario=text_value))


def entrar(request):
    """Realiza o Log-in caso o usuario ou o email e a senha passados através dos input's 
    forem as mesmas contidas no banco de dados. Se caso não forem, retorna uma mensagem no HTML."""

    user_email = request.POST.get("user_email")
    password = request.POST.get("password")
    
    
    bool_, mensagem = False, ""

    # Se o usuario existir no Banco de Dados
    if searchUser_Email(user_email, "usuario").exists():
        # Compara a senha do usuario no banco com a senha passada no input
        if searchUser_Email(user_email, "usuario")[0].senha == password:
            if searchUser_Email(user_email, "usuario")[0].admin == None:
                # Retorna pro HTML manage.html como administrador
                return redirect(manager)
            else:
                return redirect(home)
        else: bool_, mensagem = True, "Senha incorreta!"

    elif None in [user_email, password]: bool_= False

    else: bool_, mensagem = True, "E-mail ou usuário não existe!"

    users = Usuario.objects.all()
    return render(request, "entry.html", {"bool": bool_,"d-none":"", "mensagem": mensagem, "users": users})
    

def editar(request, id):
    """A partir do id do usuario, atualiza as informações do usuario contidas no banco de dados com os dados passados nos input's."""

    name = request.POST.get("nome")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("senha")
    isAdmin = request.POST.get("isAdmin")
    print('TBETYHN = ', isAdmin)

    user = Usuario.objects.filter(id=id).update(
        nome=name,
        usuario=username,
        email=email,
        senha=password,
        admin=isAdmin
        )
    return redirect(manager)




    
# def download_db(request):
#     """ """
#     con = sqlite3.connect("db.sqlite3")

#     db_df = pd.read_sql_query("SELECT * FROM movie", con)
#     db_df.to_csv('./new_database.csv', index=False)
    