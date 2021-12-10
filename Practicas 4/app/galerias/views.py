from django.shortcuts import render, HttpResponse
from django.contrib import messages

from .forms import *
from .models import Cuadro, Galeria

import logging
logger = logging.getLogger('django')


def index(request):
    context = {}
    return render(request, 'index.html', context)


def mostrar_galerias(request):
    galerias = Galeria.objects.all()
    context = {
        "galerias": galerias
    }
    return render(request, 'index.html', context)

# ────────────────────────────────────────────────────────────────────────────────


def crear_cuadro(request):
    if 'nombre' in request.POST:
        form = CrearCuadroForm(request.POST, request.FILES)

        if form.is_valid():
            nombre_cuadro = form['nombre'].value()

            if Cuadro.objects.filter(nombre=nombre_cuadro).exists():
                messages.error(request, 'Este cuadro ya existe en la base de datos.')
            else:
                form.save()
                form = CrearCuadroForm()
    else:
        form = CrearCuadroForm()

    return render(request, 'index.html', {'crear_cuadro_form': form})


def crear_galeria(request):
    if 'nombre' in request.POST:
        form = CrearGaleriaForm(request.POST)

        if form.is_valid():
            nombre_galeria = form['nombre'].value()

            if Galeria.objects.filter(nombre=nombre_galeria).exists():
                messages.error(request, 'Esta galería ya existe en la base de datos.')
            else:
                form.save()
                form = CrearGaleriaForm()

    else:
        form = CrearGaleriaForm()

    return render(request, 'index.html', {'crear_galeria_form': form})


# ────────────────────────────────────────────────────────────────────────────────


def borrar_galeria(request):
    form = SeleccionarGaleria(request.POST)

    if form.is_valid():
        Galeria.objects.filter(id = form['galerias'].value()).delete()

    return render(request, 'index.html', {'seleccionar_galeria_form': SeleccionarGaleria()})


def borrar_cuadro(request):
    form = SeleccionarCuadro(request.POST)

    if form.is_valid():
        Cuadro.objects.filter(id = form['cuadros'].value()).delete()

    return render(request, 'index.html', {'seleccionar_cuadro_form': SeleccionarCuadro()})


# ────────────────────────────────────────────────────────────────────────────────


def actualizar_galeria(request, pk):
    if pk:
        instancia = Galeria.objects.get(pk = pk)
    else:
        instancia = None

    form = CrearGaleriaForm(request.POST, instance=instancia)

    if form.is_valid():
        form.save()

    return render(request, 'index.html')


def actualizar_cuadro(request, pk):
    if pk:
        instancia = Cuadro.objects.get(pk = pk)
    else:
        instancia = None

    form = CrearCuadroForm(request.POST, instance=instancia)

    if form.is_valid():
        form.save()

    return render(request, 'index.html')


def formulario_edit_galeria(request):
    form = SeleccionarGaleria(request.POST)

    context = {}

    if form.is_valid():
        instancia = Galeria.objects.get(id = form['galerias'].value())
        context['actualizar_galeria_form'] = CrearGaleriaForm(instance = instancia)
        context['id_galeria'] = instancia.id
    else:
        context['seleccionar_galeria_form'] = SeleccionarGaleria()

    return render(request, 'index.html', context)


def formulario_edit_cuadro(request):
    form = SeleccionarCuadro(request.POST)

    context = {}

    if form.is_valid():
        instancia = Cuadro.objects.get(id = form['cuadros'].value())
        context['actualizar_cuadro_form'] = CrearCuadroForm(instance = instancia)
        context['id_cuadro'] = instancia.id
    else:
        context['seleccionar_cuadro_form'] = SeleccionarCuadro()

    return render(request, 'index.html', context)