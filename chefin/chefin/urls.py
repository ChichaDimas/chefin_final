from django.contrib import admin
from django.urls import path, include
from store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
    path('chefin/', include('store.urls')),

    path('profile/', profile, name='profile'),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),

    # path('basket_remove/<int:basket_id>/', basket_remove, name='basket_remove'),

    path('basket_remove/<int:product_id>/', basket_remove, name='basket_remove'),

    path('add_to_cart/', add_to_cart, name='add_to_cart'),
]
