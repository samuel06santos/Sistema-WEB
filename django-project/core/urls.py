from django.contrib import admin
from django.urls import path
from .views import home, search, salvar, deletar, entrar, registrar
#, update

urlpatterns = [
    path('', home, name="search"),
    path('login/', entrar, name="login"),
    path('salvar/', salvar, name="salvar"),
    path('registrar/', registrar, name="registrar"),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('search/', search, name='search'), #<str:search>
]
