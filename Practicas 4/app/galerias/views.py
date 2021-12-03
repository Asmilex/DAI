from django.shortcuts import render, HttpResponse

from .forms import CrearCuadroForm, CrearGaleriaForm

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
             return None
    else:
        form = CrearCuadroForm()

    return render(request, 'index.html', {'crear_cuadro_form': form})


def crear_galeria(request):
    if request.method == 'POST':
        form = CrearGaleriaForm(request.POST)

        if form.is_valid():
             return None
    else:
        form = CrearGaleriaForm()

    return render(request, 'index.html', {'crear_galeria_form': form})