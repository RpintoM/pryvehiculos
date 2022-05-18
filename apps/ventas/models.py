from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from apps.vehiculos.models import Vehiculos
    

# Create your models here.


class Ventas(models.Model):
    fecha = models.DateField()
    valorTotal = models.BigIntegerField()
    tipoPago = models.CharField(max_length=20)
    user =  models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    vehiculo = models.ManyToManyField(Vehiculos,through='VehiculoVenta')
    
class VehiculoVenta(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, blank=False, null=False, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, blank=False, null=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.BigIntegerField()
    