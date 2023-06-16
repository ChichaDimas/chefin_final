from django.shortcuts import render

# Create your views here.

def menu(request):

    context = {
        'title': 'Store - магазин',

    }
    return render(request, 'store/base.html', context)
