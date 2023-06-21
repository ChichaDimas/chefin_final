
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
        'title': 'Магазин - Роли',
        'products': products,
    }

    return render(requests, 'store/rolu.html', context)


def pizza(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Піца',
        'products': products,
    }

    return render(requests, 'store/pizza.html', context)

def salat(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Салати',
        'products': products,
    }

    return render(requests, 'store/salat.html', context)

def osnovni(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Основні страви',
        'products': products,
    }

    return render(requests, 'store/osnovni.html', context)

def soups(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Супи',
        'products': products,
    }

    return render(requests, 'store/soups.html', context)


def zakyski(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Закуски',
        'products': products,
    }

    return render(requests, 'store/zakyski.html', context)


def garniry(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Гарніри',
        'products': products,
    }

    return render(requests, 'store/garniry.html', context)

def hot(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Гарячі страви',
        'products': products,
    }

    return render(requests, 'store/hot.html', context)

def cold_drinks(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Холодні напої',
        'products': products,
    }

    return render(requests, 'store/cold_drinks.html', context)
def beer(requests):
    products = Product.objects.all()

    context = {
        'title': 'Магазин - Розливне пиво',
        'products': products,
    }

    return render(requests, 'store/beer.html', context)