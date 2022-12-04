from django.db import models

# Create your models here.

class Usuario(models.Model):
    NombreUsuario = models.CharField(max_length=20)
    ApellidoUsuario = models.CharField(max_length=20)
    FechaNacimiento = models.DateField()
    Direccion = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=15)
    Usuario = models.EmailField(max_length=30)
    Contrasena  = models.CharField(max_length=8) 
    
class Traslados(models.Model):
    Mes = models.CharField(max_length=10)
    Cantidad = models.FloatField()
    
class Ambulancias(models.Model):
    Identificacion = models.CharField(max_length=20)
    TipoHerida = models.CharField(max_length=20)
    CantidadH = models.FloatField()
    
    
    