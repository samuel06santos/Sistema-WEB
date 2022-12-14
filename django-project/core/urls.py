from django.contrib import admin
from django.urls import path
from .views import search, salvar, deletar, entrar, registrar, manager, editar, logout #, download_db

urlpatterns = [
    path('', entrar, name="search"),                    # Tela principal (home)
    path('manage/', manager, name="search"),            # "Tela do administrador"
    path('search/', search, name='search'),             # Url de pesquisa
    path('salvar/', salvar, name="salvar"),             # Url de Salvar
    path('deletar/<int:id>/', deletar, name='deletar'), # Url de Deletar
    path('editar/<int:id>/', editar, name='editar'),    # Url de Editar
    path('registrar/', registrar, name="registrar"),    # Url de Registrar
    path('login/', entrar, name="login"),               # Tela de Login
    path('logout/', logout),                            # Tela de LogOut
    # path("manage/", download_db)
]
