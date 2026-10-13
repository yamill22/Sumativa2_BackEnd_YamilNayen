from django.db import models

class editorial(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre

class libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editorial = models.ForeignKey(editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    precio = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo