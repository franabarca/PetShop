from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer
import requests

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer




def home(request):
    

    return render(request, 'pet/index.html')

def index(request):
    if request.user.is_authenticated:
        comprador = request.user.comprador
        pedido, created = Pedido.objects.get_or_create(comprador=comprador, complete=False)
        items = pedido.itempedido_set.all()
        carritoItems = pedido.get_carrito_items

    else: 
        items = []
        pedido = {'get_carrito_total': 0,'get_carrito_items':0}
        carritoItems = pedido['get_carrito_items']
    
    context = {'productos': productos, 'carritoItems':carritoItems}
    return render(request, 'pet/index.html', context)

def donar(request):

    return render(request, 'pet/index2.html')

def contacto(request):

    data = {
        'form' : ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        
        else:
            data["form"] = formulario

    return render(request, 'pet/contacto.html', data)

def productos(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/', headers={'Authorization': 'Token e865ab7e81df268d719cbba968fae9fef9949c6e'}).json()

    
    data = {
        'productos': response
    }

    return render(request, 'pet/productos.html', data)

def carrito(request):

    if request.user.is_authenticated:
        comprador = request.user.comprador
        pedido, created = Pedido.objects.get_or_create(comprador=comprador, complete=False)
        items = pedido.itempedido_set.all()
    else: 
        items = []
        pedido = {'get_carrito_total': 0,'get_carrito_items':0}
        
    context = {'items': items, 'pedido': pedido}
    return render(request, 'pet/carrito.html', context)

def checkout(request):
    
    if request.user.is_authenticated:
        comprador = request.user.comprador
        pedido, created = Pedido.objects.get_or_create(comprador=comprador, complete=False)
        items = pedido.itempedido_set.all()
        carritoItems = pedido.get_carrito_items

    else: 
        items = []
        pedido = {'get_carrito_total': 0,'get_carrito_items':0}
        items = pedido.itempedido_set.all()
        carritoItems = pedido.get_carrito_items
        
    context = {'items': items, 'pedido': pedido,'productos': productos, 'carritoItems':carritoItems}
    return render(request, 'pet/checkout.html', context)

@permission_required('app.add_producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario

    return render(request, 'pet/producto/agregar.html', data)

#envio de productos hacia el template
@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'pet/producto/listar.html', data)

@permission_required('app.change_producto')
def modificar_producto(request, id):
#el get_object_or_404 es para buscar producto
    producto = get_object_or_404(Producto, id=id)
#el instance rellena el formulario
    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_productos")
            
        data["form"] = formulario

    return render(request, 'pet/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_productos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)
    