from django.http import HttpResponse, HttpRequest


def product_index(request):
    return HttpResponse("Hello, world. You're at the product index.")
