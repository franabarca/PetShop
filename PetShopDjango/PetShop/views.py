from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'C:/ProyectosDjango/PetShopDjango/PetShop/templates/PetShop/index.html')