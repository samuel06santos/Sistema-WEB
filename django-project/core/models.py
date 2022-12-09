from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, default="", null=True)
    usuario = models.CharField(max_length=50, default="", null= True)
    email = models.EmailField(max_length=100, default="", null=True)
    senha = models.CharField(max_length=50, default="", null=True)
    
    def __str__(self):
        return self.nome