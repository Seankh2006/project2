from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import CharField


class User(AbstractUser):
    pass

class listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    date = models.DateField()
    img = models.CharField(max_length=1000)