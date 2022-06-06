from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm
from django.contrib import messages

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
            messages.success(request, "guardado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'pet/producto/agregar.html', data)

#envio de productos hacia el template
def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'pet/producto/listar.html', data)


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
            return redirect(to="listar_productos")
            
        data["form"] = formulario

    return render(request, 'pet/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")