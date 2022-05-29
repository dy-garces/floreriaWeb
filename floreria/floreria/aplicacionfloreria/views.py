from itertools import product
from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.
def home(request):   
    return render(request,'aplicacionfloreria/home.html')

def flores(request):
    productos = Producto.objects.all()
    categoria = Categoria.objects.all()
    contexto = {
        'productos': productos,
        'categoria': categoria
    }
    return render(request,'aplicacionfloreria/flores.html',contexto)

def plantas(request):
    productos = Producto.objects.all()
    categoria = Categoria.objects.all()
    contexto = {
        'productos': productos,
        'categoria': categoria
    }
    return render(request,'aplicacionfloreria/plantas.html',contexto)

def arboles(request):
    productos = Producto.objects.all()
    categoria = Categoria.objects.all()
    contexto = {
        'productos': productos,
        'categoria': categoria
    }
    return render(request,'aplicacionfloreria/arboles.html',contexto)

def maceteros(request):
    productos = Producto.objects.all()
    categoria = Categoria.objects.all()
    contexto = {
        'productos': productos,
        'categoria': categoria
    }
    return render(request,"aplicacionfloreria/maceteros.html",contexto)

def jardineria(request):
    productos = Producto.objects.all()
    categoria = Categoria.objects.all()
    contexto = {
        'productos': productos,
        'categoria': categoria
    }
    return render(request,"aplicacionfloreria/jardineria.html",contexto)

def contacto(request):

    return render(request,"aplicacionfloreria/contacto.html")

def quienesSomos(request):

    return render(request,"aplicacionfloreria/quienesSomos.html")