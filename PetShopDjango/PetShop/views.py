from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):

    return render(request, 'pet/index.html')

def index(request):

    return render(request, 'pet/index.html')

def donar(request):

    return render(request, 'pet/index2.html')

def ofertas(request):

    return render(request, 'pet/ofertas.html')

def productos(request):

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'pet/productos.html', data)
