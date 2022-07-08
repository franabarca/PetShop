from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio", "marca"]
    list_editable= ["precio"]
    search_fields = ["nombre"]
    list_filter =["marca"]



admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Comprador)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(DireccionEnvio)
