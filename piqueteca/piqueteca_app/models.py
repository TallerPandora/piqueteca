from django.db import models

class Autora(models.Model):
	nombre = models.CharField(max_length=200)
	contacto = models.CharField(max_length=200, null=True, blank=True)

class Lectora(models.Model):
	nombre = models.CharField(max_length=200)
	correo = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200, null=True, blank=True)

class Estado_libro(models.Model):
	estado = models.CharField(max_length=200)

class Estado_prestamo(models.Model):
	estado = models.CharField(max_length=200)

class Editorial(models.Model):
	nombre = models.CharField(max_length=200)
	contacto = models.CharField(max_length=200)

class Licencia(models.Model):
	licencia = models.CharField(max_length=200)

class Categoria(models.Model):
	nombre = models.CharField(max_length=200)

class Libro(models.Model):
	titulo = models.CharField(max_length=200)
	autora = models.ManyToMany(Autora)
	anio_edicion = models.Integer()
	editorial = models.ForeignKey(Editorial)
	resenia = models.CharField(max_length=3000, null=True, blank=True)
	categoria = models.ManyToMany(Categoria)
	enlace_descarga = models.CharField(Max_length=200, null=True, blank=True)
	estado = models.ForeignKey(Estado_libro)
	licencia = models.ForeignKey(Licencia)

class Prestamos(models.Model)
	libros = models.ManyToMany(Libro)
	lectora = models.ForeignKey(Lectora)
	fecha_prestamo = models.DateTimeField(auto_now=True)
	fecha_devolucion = models.DateTimeField()
	estado = models.ForeignKey(Estado_prestamo)

