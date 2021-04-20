from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse


# Create your models here.

class UsuarioPers(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    genero = models.CharField(null=True,blank=True, max_length=1)


class Post(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
   
    def __str__(self):
        return self.text
   

class Manga(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
   
    def __str__(self):
        return self.text

    

class DescripLib(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
    presio = models.TextField(default="")
   
    def __str__(self):
        return self.text

class Autores(models.Model):
    Nombre = models.TextField(default="")
    Descripcion = models.TextField(default="")
    img = models.TextField(default="")
    Nacionalidad = models.TextField(default="")
    F_Muerte = models.TextField(default="")
    autor = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])

class Comentario(models.Model):
    comentario = models.CharField(max_length=300)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name='comentario'
        )
        
    def __str__(self):
        return self.comentario
    

