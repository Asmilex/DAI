from django.db import models
from django.utils import timezone

class Galeria(models.Model):
    nombre    = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Cuadro(models.Model):
    nombre         = models.CharField(max_length=200)
    galeria        = models.ForeignKey(Galeria, on_delete=models.CASCADE)
    autor          = models.CharField(max_length=200)
    fecha_creacion = models.DateField(default=timezone.now)
    imagen         = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.nombre + ", de " + self.autor