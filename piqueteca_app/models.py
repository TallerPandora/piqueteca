from django.db import models

class Autora(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    contacto = models.CharField(max_length=200, null=True, blank=True)

class Lectora(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
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

class Tipo(models.Model):
    tipo = models.CharField(max_length = 200)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autora = models.ManyToManyField(Autora)
    anio_edicion = models.IntegerField()
    editorial = models.ForeignKey(Editorial)
    resenia = models.CharField(max_length=3000, null=True, blank=True)
    categoria = models.ManyToManyField(Categoria)
    enlace_descarga = models.CharField(max_length=200, null=True, blank=True)
    estado = models.ForeignKey(Estado_libro)
    licencia = models.ForeignKey(Licencia)
    tipo = models.ForeignKey(Tipo)

    def get_autoras(self):
        autoras = Libro.objects.get(id=self.id).autora.all()
        lista_autoras = ""
        for autora in autoras:
            lista_autoras += autora.nombre + " " + autora.apellido + " | "
        return lista_autoras
    get_autoras.short_description = 'Autor/a'

class Prestamos(models.Model):
    libros = models.ManyToManyField(Libro)
    lectora = models.ForeignKey(Lectora)
    fecha_prestamo = models.DateTimeField(auto_now=True)
    fecha_devolucion = models.DateTimeField()
    estado = models.ForeignKey(Estado_prestamo)

