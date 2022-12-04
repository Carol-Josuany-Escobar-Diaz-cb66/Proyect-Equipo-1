from django.contrib import admin
from .models import Usuario, Traslados, Ambulancias
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Traslados)
admin.site.register(Ambulancias)