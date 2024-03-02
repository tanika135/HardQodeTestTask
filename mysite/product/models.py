from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ManyToManyField(User)
    min_users = models.IntegerField(default=1)
    max_users = models.IntegerField(default=100)


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    link_to_video = models.CharField(max_length=100)


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User)

