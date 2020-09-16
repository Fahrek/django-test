from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'home.html')

def menu_infantil(request):
    return render(request, 'menu_infantil.html')

def receta_facil(request):
    return render(request, 'receta_facil.html')

def mafe(request):
    return render(request, 'mafe.html')

def feijoada(request):
    return render(request, 'feijoada.html')

def pizza(request):
    return render(request, 'pizza.html')

def canelones(request):
    return render(request, 'canelones.html')

def flor_de_calabacin(request):
    return render(request, 'flor_de_calabacin.html')

def gazpacho(request):
    return render(request, 'gazpacho.html')

def noodles(request):
    return render(request, 'sopa_de_noodles.html')

def ensaladilla_rusa(request):
    return render(request, 'ensaladilla_rusa.html')

def carbonara(request):
    return render(request, 'carbonara.html')
