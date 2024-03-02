from django.contrib import admin
from .models import Product, Lesson, Group


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
