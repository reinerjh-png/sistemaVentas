# clientes/models.py
from django.db import models

class Cliente(models.Model):
    ruc = models.CharField(max_length=11, unique=True, blank=True, null=True)  # opcional inicialmente
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.ruc:
            return f"{self.nombre} ({self.ruc})"
        return self.nombre
