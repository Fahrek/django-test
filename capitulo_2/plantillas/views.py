from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home_page_view(request):
    return render(request, 'hola_mundo.html')

def about_page_view(request):
    randnum_fav = random.randrange(100)
    parametros = {'numero_favorito': randnum_fav}
    return render(request, 'about.html', parametros)

def home(request):
    doc = """
                <!DOCTYPE html>
                <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <title>Home</title>
                </head>
                <body>
                    <nav>
                        <a href="{% url 'home' %}"> home </a>
                        <a href="{% url 'inicio' %}"> contact </a>
                        <a href="{% url 'about' %}"> about </a>
                    </nav>
                    
                    <h1>Hola Mundo 2!!</h1>
                    <p>Esto es un párrafo en HTML</p>
                </body>
                </html>
          """

    return HttpResponse(doc)
