from django.urls import path

from . import views

urlpatterns = [
    path("", views.product_index, name="product_index"),
]
