from django.db import models


class Datos(models.Model):
    temperatura = models.DecimalField(max_digits=10, decimal_places=2)
    humedad = models.DecimalField(max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now_add=True)

class MoverRobot(models.Model):
    accion = models.IntegerField() 
