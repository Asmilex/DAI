from django import forms
from .models import Cuadro, Galeria

# Cómo crear correctamente los formularios
# https://stackoverflow.com/questions/22739701/django-save-modelform

class CrearGaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = '__all__'

class CrearCuadroForm(forms.ModelForm):
    #https://docs.djangoproject.com/en/3.2/ref/forms/api/#binding-uploaded-files
    class Meta:
        model = Cuadro
        fields = '__all__'