from django.contrib import admin
from django.urls import path
from .views import search, salvar, deletar, entrar, registrar, manager, editar, sla

urlpatterns = [
    path('', manager, name="search"),   # Será a tela principal (home)
    path('manage/', manager, name="search"), # "tela do administrador"
    path('search/', search, name='search'),
    path('salvar/', salvar, name="salvar"),
    path('deletar/<int:id>/', deletar, name='deletar'),
    path('registrar/', registrar, name="registrar"), 
    path('login/', entrar, name="login"),
    path('editar/<int:id>/', editar, name='editar'),
    path('sla/', sla)
]
