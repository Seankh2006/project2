from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class category(models.Model):
    categorylist = models.CharField(max_length=64)
    def __str__(self):
        return self.categorylist

class listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    date = models.DateField()
    img = models.CharField(max_length=1000)
    categorylist1 = models.ForeignKey(category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="owner")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="watchlist2")
    def __str__(self):
        return self.title


