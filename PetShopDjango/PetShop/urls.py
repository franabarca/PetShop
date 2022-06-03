from django.urls import path
from .views import home, ofertas, donar, index

urlpatterns = [
    path('', home,name='home'),
    path('pet/index.html', index,name='index'),
    path('pet/index2.html', donar,name='donar'),
    path('pet/ofertas.html', ofertas,name='ofertas'),
]
