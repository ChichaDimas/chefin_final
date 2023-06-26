from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from chefin.settings import POSTER_POS_API_KEY
from django.shortcuts import render
from .helpers import *
from .models import *
import requests
from chefin.settings import POSTER_POS_API_KEY
from cloudipsp import Api, Checkout
from django.shortcuts import render,HttpResponseRedirect
from .helpers import *
from .models import *
from store.templatetags.custom_filters import mul_price
from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.cache import cache






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
        'title': 'Chefin',
        'products': products,
    }

    return render(request, 'store/base.html', context)

def rolu(requests):
    products = Product.objects.all()

    context = {
        'title': 'Роли',
        'products': products,
    }

    return render(requests, 'store/rolu.html', context)


def pizza(requests):
    products = Product.objects.all()

    context = {
        'title': 'Піца',
        'products': products,
    }

    return render(requests, 'store/pizza.html', context)

def salat(requests):
    products = Product.objects.all()

    context = {
        'title': 'Салати',
        'products': products,
    }

    return render(requests, 'store/salat.html', context)

def osnovni(requests):
    products = Product.objects.all()

    context = {
        'title': 'Основні страви',
        'products': products,
    }

    return render(requests, 'store/osnovni.html', context)

def soups(requests):
    products = Product.objects.all()

    context = {
        'title': 'Супи',
        'products': products,
    }

    return render(requests, 'store/soups.html', context)


def zakyski(requests):
    products = Product.objects.all()

    context = {
        'title': 'Закуски',
        'products': products,
    }

    return render(requests, 'store/zakyski.html', context)


def garniry(requests):
    products = Product.objects.all()

    context = {
        'title': 'Гарніри',
        'products': products,
    }

    return render(requests, 'store/garniry.html', context)

def hot(requests):
    products = Product.objects.all()

    context = {
        'title': 'Гарячі страви',
        'products': products,
    }

    return render(requests, 'store/hot.html', context)

def cold_drinks(requests):
    products = Product.objects.all()

    context = {
        'title': 'Холодні напої',
        'products': products,
    }

    return render(requests, 'store/cold_drinks.html', context)
def beer(requests):
    products = Product.objects.all()

    context = {
        'title': 'Розливне пиво',
        'products': products,
    }

    return render(requests, 'store/beer.html', context)


def dostavka_ta_oplata(requests):

    context = {
        'title': 'Доставка та оплата',

    }

    return render(requests, 'store/dostavka_ta_oplata.html', context)







def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    request.session.setdefault('basket', {})
    basket = request.session['basket']
    basket[product_id] = product.to_json()  # преобразование объекта Product в JSON
    request.session.modified = True

    return JsonResponse({'success': True})




def basket_remove(request, basket_id):
    # Удаление корзины из кеша
    cache_key = f"basket_{basket_id}"
    cache.delete(cache_key)

    # Ваш дальнейший код...
    return redirect('basket')





def profile(request):
    # Получаем текущую корзину из сессии пользователя
    basket = request.session.get('basket', {})
    basket_items = basket.values()
    print(basket_items)
    context = {
        'title': 'Корзина',
        'baskets': basket_items,
        'mul_price': mul_price,
        'savedValue': 1,
    }
    return render(request, 'store/baskets.html', context)





def add_to_cart(request):
    api = Api(merchant_id=1397120,
              secret_key='Not for tests. Test credentials: https://docs.fondy.eu/docs/page/2/ ')
    checkout = Checkout(api=api)
    data = {
        "currency": "UAH",
        "amount": 12000
    }
    url = checkout.url(data).get('checkout_url')
    context = {
        'title':'Store',
        'url': url
    }
    return render(request,'store/add_to_cart.html',context)