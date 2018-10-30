from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title   



class Registrado(models.Model):
    nombre = models.CharField(max_length=13, blank=False, null=True)
    email = models.EmailField()
    rut = models.CharField(max_length=13, blank=False, null=True)
    fechaNacimiento = models.DateTimeField(null = True)
    telefono = models.IntegerField(null=True)
    region = models.CharField(max_length=13, blank=False, null=True)
    ciudad = models.CharField(max_length=13, blank=False, null=True)
    tipoVivienda = models.CharField(max_length=13, blank=False, null=True)
    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email