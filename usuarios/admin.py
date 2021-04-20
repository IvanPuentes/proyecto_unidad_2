from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioPersCreationForm, UsuarioPersChangeForm
from .models import UsuarioPers,Post,Manga,DescripLib,Autores,Comentario

class ComentarioInLine(admin.TabularInline):
    model = Comentario

class UsuarioPersAdmin(UserAdmin):
    add_form = UsuarioPersCreationForm
    form = UsuarioPersChangeForm
    model = UsuarioPers
    list_display = ['email', 'username', 'edad' , 'telefono','genero', 'is_staff',]

# Register your models here.

admin.site.register(UsuarioPers,UsuarioPersAdmin)
admin.site.register(Post)
admin.site.register(Manga)
admin.site.register(DescripLib)
admin.site.register(Autores)
admin.site.register(Comentario)