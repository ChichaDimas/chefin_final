
from chefin.settings import POSTER_POS_API_KEY
from django.shortcuts import render
from .helpers import *
from .models import *
import requests




def menu(request):
    api_key = POSTER_POS_API_KEY
    fill_database(api_key)

    query = request.GET.get('query')
    category = request.GET.get('category')

    products = Product.objects.all()
    print(products)

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category__icontains=category)

    context = {
        'title': 'Store - магазин',
        'products': products,
    }

    return render(request, 'store/base.html', context)

def rolu(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Роллы',
        'products': products,
    }

    return render(requests, 'store/rolu.html', context)
