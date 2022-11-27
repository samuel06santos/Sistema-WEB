from django.contrib import admin
from django.urls import path
from .views import home, salvar, deletar, edit, update

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='edit'),
    
]