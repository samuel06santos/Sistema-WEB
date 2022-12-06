from django.contrib import admin
from django.urls import path
from .views import home, entrar, registrar, salvar, deletar
#, edit, update

urlpatterns = [
    path('', home,  name="search"),
    path('login/', entrar, name="login"),
    path('salvar/', salvar, name="salvar"),
    path('registrar/', registrar, name="registrar"),
    path('deletar/<int:id>', deletar, name='deletar'),
    # path('edit/<int:id>', edit, name='edit'),
    # path('update/<int:id>', update, name='edit'),
]