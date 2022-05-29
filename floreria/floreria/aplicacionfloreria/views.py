from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'aplicacionfloreria/home.html')

def flores(request):
    return render(request,'aplicacionfloreria/flores.html')

def plantas(request):
    return render(request,'aplicacionfloreria/plantas.html')

def arboles(request):
    return render(request,'aplicacionfloreria/arboles.html')

def maceteros(request):
    return render(request,"aplicacionfloreria/maceteros.html")

def jardineria(request):
    return render(request,"aplicacionfloreria/jardineria.html")

def contacto(request):
    return render(request,"aplicacionfloreria/contacto.html")

def quienesSomos(request):
    return render(request,"aplicacionfloreria/quienesSomos.html")