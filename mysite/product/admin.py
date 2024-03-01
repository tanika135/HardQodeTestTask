from django.contrib import admin
from .models import Product, Lesson


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ['id']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    ordering = ['id']

