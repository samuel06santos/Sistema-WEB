from django.db import models

class Usuario(models.Model):
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user