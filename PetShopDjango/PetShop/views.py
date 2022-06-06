from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm, ProductoForm

# Create your views here.

def home(request):

    return render(request, 'pet/index.html')

def index(request):

    return render(request, 'pet/index.html')

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

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'pet/productos.html', data)

def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'pet/producto/agregar.html', data)
