from django import forms
from .models import Cuadro

class CrearGaleriaForm(forms.Form):
    nombre = forms.CharField(max_length = 200)
    direccion = forms.CharField(max_length = 200)

class CrearCuadroForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    galeria = forms.ModelChoiceField(queryset=Cuadro.objects.all(), to_field_name='nombre')
    autor = forms.CharField(max_length=200)
    fecha = forms.DateField()
    imagen = forms.ImageField() #https://docs.djangoproject.com/en/3.2/ref/forms/api/#binding-uploaded-files