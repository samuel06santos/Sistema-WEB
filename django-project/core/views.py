from django.shortcuts import render, redirect
from .models import Usuario
from django.db.models import Q
import requests

def home(request):
    # search = request.POST.get("search")
    # users = Usuario.objects.filter(user=search)

    users = Usuario.objects.all()
    return render(request, "home.html", {"usuarios": users})

def search(request):
    search = request.POST.get("search")
    print(search)
    users = Usuario.objects.filter(Q(user__startswith=search))
    return render(request, "home.html", {"usuarios": users})

def entrar(request):
    email = request.POST.get("email")
    
    password = request.POST.get("password")
    print(email, password, sep="\n")
    return render(request, "login.html")

def registrar(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    print(f"USUARIO CRIADO:\n{email=}\n{password=}\n\n")
    return render(request, "entry.html")

def salvar(request):
    user = request.POST.get("name")
    dict_info = requests.get(f"https://api.github.com/users/{user}").json()

    names = dict_info["name"].split() if dict_info["name"] is not None else ['','']
    print(names)
    Usuario.objects.create(user=user, first_name=names[0], last_name=names[1])
    return redirect(home)

def deletar(request, id):
    user = Usuario.objects.get(id=id)
    user.delete()
    return redirect(home)

# def edit(request, id):
#     user = Usuario.objects.get(name=search)
#     return render(request, "edit.html", {"usuario": user})

# EM CONSTRUÇÃO

# def update(request, id):
#     new_name = request.POST.get("name")
#     user = Usuario.objects.get(id=id)
#     user.name = new_name
#     user.save()
#     return redirect(home)

