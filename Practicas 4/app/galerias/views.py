from django.shortcuts import render, HttpResponse
from django.contrib import messages

from .forms import CrearCuadroForm, CrearGaleriaForm
from .models import Cuadro, Galeria

import logging
logger = logging.getLogger('django')


def index(request):
    context = {}
    return render(request, 'index.html', context)

""" def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)
 """

def crear_cuadro(request):
    if request.method == 'POST':
        form = CrearCuadroForm(request.POST)

        if form.is_valid():
            nombre_cuadro = form['nombre'].value()

            if Cuadro.objects.filter(nombre=nombre_cuadro).exists():
                messages.error(request, 'Este cuadro ya existe en la base de datos.')
            else:
                form.save()
    else:
        form = CrearCuadroForm()

    return render(request, 'index.html', {'crear_cuadro_form': form})


def crear_galeria(request):
    if request.method == 'POST':
        form = CrearGaleriaForm(request.POST)

        if form.is_valid():
            nombre_galeria = form['nombre'].value()

            if Galeria.objects.filter(nombre=nombre_galeria).exists():
                messages.error(request, 'Esta galería ya existe en la base de datos.')
            else:
                form.save()

    else:
        form = CrearGaleriaForm()

    return render(request, 'index.html', {'crear_galeria_form': form})


def borrar_galeria(request):
    pass

def borrar_cuadro(request):
    pass

def actualizar_galeria(request):
    pass

def actualizar_cuadro(request):
    pass