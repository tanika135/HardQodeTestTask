from django.db import models


class Product(models.Model):
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Lesson(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    link_to_video = models.CharField(max_length=100)


