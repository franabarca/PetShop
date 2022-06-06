from django import forms
from .models import Contacto, Producto

# Declara formulario con python
class ContactoForm(forms.ModelForm):
    # aqui se toman los datos desde el modelo definido
    class Meta:
        model= Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


