from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'pet/index.html')

def index(request):

    return render(request, 'pet/index.html')

def donar(request):

    return render(request, 'pet/index2.html')

def ofertas(request):

    return render(request, 'pet/ofertas.html')

