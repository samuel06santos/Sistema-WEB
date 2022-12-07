from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, default = "")
    last_name = models.CharField(max_length=50, default = "")
    email = models.CharField(max_length=50, default = "")
    senha = models.CharField(max_length=50, default = "")
    def __str__(self):
        return self.user
