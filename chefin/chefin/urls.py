from django.contrib import admin
from django.urls import path, include
from store.views import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
    path('chefin/', include('store.urls')),
]
