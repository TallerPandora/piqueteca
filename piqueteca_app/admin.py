from django.contrib import admin
from piqueteca_app.models import *

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'get_autoras']

class AutoraAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido']

admin.site.register(Libro, LibroAdmin)
admin.site.register(Autora, AutoraAdmin)
admin.site.register(Lectora)
admin.site.register(Estado_libro)
admin.site.register(Estado_prestamo)
admin.site.register(Editorial)
admin.site.register(Licencia)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Prestamos)

