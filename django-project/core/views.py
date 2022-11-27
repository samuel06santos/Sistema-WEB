from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    users = Usuario.objects.all()
    return render(request, "home.html", {"usuarios": users})

def salvar(request):
    name = request.POST.get("name")
    Usuario.objects.create(user=name)
    return redirect(home)

def deletar(request, id):
    user = Usuario.objects.get(id=id)
    user.delete()
    return redirect(home)

# EM CONSTRUÇÃO

def edit(request, id):
    user = Usuario.objects.get(id=id)
    return render(request, "edit.html", {"usuario": user})

def update(request, id):
    new_name = request.POST.get("name")
    user = Usuario.objects.get(id=id)
    user.name = new_name
    user.save()
    return redirect(home)

