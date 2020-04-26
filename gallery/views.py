from django.shortcuts import render
from . import models


def all_products(request):
    products = models.Product.objects.all()
    return render(request, 'gallery/all_products.html', {'products': products})