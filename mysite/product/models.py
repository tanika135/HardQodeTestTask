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


class ProductAccess(models.Model):
    """
    Модель для хранения информации, есть ли доступ к продукту у пользователя
    """
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

