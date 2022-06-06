from django.urls import path
from .views import home, contacto, donar, index, productos, agregar_producto
urlpatterns = [
    path('', home,name='home'),
    path('pet/index.html', index,name='index'),
    path('pet/index2.html', donar,name='donar'),
    path('pet/contacto.html', contacto,name='contacto'),
    path('pet/productos.html', productos,name='productos'),
    path('agregar-producto/', agregar_producto,name='agregar_producto'),
]
