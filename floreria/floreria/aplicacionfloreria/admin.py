from django.contrib import admin
from .models import Categoria,Producto,Region,Comuna

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)