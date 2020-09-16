from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home_page_view(request):
    numrand_fav = random.randrange(100)
    parametros = {'numero_favorito': numrand_fav}
    return render(request, 'home.html', parametros)
