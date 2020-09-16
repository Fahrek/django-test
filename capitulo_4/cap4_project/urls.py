"""cap4_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cap4_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name='home'),
    path('menu_infantil/', views.menu_infantil, name='menu'),
    path('receta_facil/', views.receta_facil, name='receta'),
    path('mafe/', views.mafe, name='mafe'),
    path('feijoada/', views.feijoada, name='feijoada'),
    path('pizza/', views.pizza, name='pizza'),
    path('canelones/', views.canelones, name='canelones'),
    path('calabacin/', views.flor_de_calabacin, name='calabacin'),
    path('gazpacho/', views.gazpacho, name='gazpacho'),
    path('noodles/', views.noodles, name='noodles'),
    path('ensaladilla/', views.ensaladilla_rusa, name='ensaladilla'),
    path('carbonara/', views.carbonara, name='carbonara'),
]
