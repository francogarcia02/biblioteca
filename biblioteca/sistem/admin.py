from django.contrib import admin
from sistem.models import Autor
from sistem.models import Libros
from sistem.models import usuarios
 
# Register your models here.
admin.site.register(Libros,)
admin.site.register(Autor,)
admin.site.register(usuarios,)
