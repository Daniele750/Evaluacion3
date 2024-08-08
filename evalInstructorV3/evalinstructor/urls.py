from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('administracion.urls')),
    path('', include('loadlists.urls')),

    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('validarHash', validarHash, name='validarHash'),
]
