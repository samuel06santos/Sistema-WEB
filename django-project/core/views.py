from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    # search = request.POST.get("search")
    # users = Usuario.objects.filter(user=search)
    users = Usuario.objects.all()
    return render(request, "home.html", {"usuarios": users})

def search(request, ):
    search = request.POST.get("search")
    users = Usuario.objects.filter(user=search)
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
    name = request.POST.get("name")
    Usuario.objects.create(user=name)
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

