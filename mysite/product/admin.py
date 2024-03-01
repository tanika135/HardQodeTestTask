from django.contrib import admin
from .models import Product, Lesson, ProductAccess, Group


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ['id']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    ordering = ['id']


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    ordering = ['id']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    ordering = ['id']
