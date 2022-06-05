from django.urls import path
from .views import home, ofertas, donar, index, productos
urlpatterns = [
    path('', home,name='home'),
    path('pet/index.html', index,name='index'),
    path('pet/index2.html', donar,name='donar'),
    path('pet/ofertas.html', ofertas,name='ofertas'),
    path('pet/productos.html', productos,name='productos'),
]
