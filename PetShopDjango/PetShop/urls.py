from django.urls import path
from .views import home, contacto, donar, index, productos, agregar_producto,\
     listar_productos, modificar_producto, eliminar_producto, registro
urlpatterns = [
    path('', home,name='home'),
    path('pet/index.html', index,name='index'),
    path('pet/index2.html', donar,name='donar'),
    path('pet/contacto.html', contacto,name='contacto'),
    path('pet/productos.html', productos,name='productos'),
    path('agregar-producto/', agregar_producto,name='agregar_producto'),
    path('listar-productos/', listar_productos,name='listar_productos'),
    path('modificar-producto/<id>/', modificar_producto,name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto,name='eliminar_producto'),
    path('registro', registro, name="registro"),
]
