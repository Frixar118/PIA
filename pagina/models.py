from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre


class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor}"
