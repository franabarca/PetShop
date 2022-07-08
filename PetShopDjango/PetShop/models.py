from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    stock = models.IntegerField(default=0,verbose_name='Stock')
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.nombre

opciones_consultas = [

    [1,"consulta"],
    [2,"reclamo"],
    [3,"sugerencia"],
    [4,"felicitaciones"],

]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class Comprador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    comprador = models.ForeignKey(Comprador, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_compra =  models.DateTimeField(auto_now_add=True)
    complete =  models.BooleanField(default=False, null=True, blank=False)
    id_transaccion =  models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_carrito_total(self):
        itemspedidos = self.itempedido_set.all()
        total = sum([item.get_total for item in itemspedidos])
        return total
    
    @property
    def get_carrito_items(self):
        itemspedidos = self.itempedido_set.all()
        total = sum([item.cantidad for item in itemspedidos])
        return total

class ItemPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_add =  models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total

class DireccionEnvio(models.Model):
    comprador = models.ForeignKey(Comprador, on_delete=models.SET_NULL, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)
    fecha_add =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion