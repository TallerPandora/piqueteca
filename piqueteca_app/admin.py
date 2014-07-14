from django.contrib import admin
from piqueteca_app.models import *

admin.site.register(Libro)
admin.site.register(Autora)
admin.site.register(Lectora)
admin.site.register(Estado_libro)
admin.site.register(Estado_prestamo)
admin.site.register(Editorial)
admin.site.register(Licencia)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Prestamos)

