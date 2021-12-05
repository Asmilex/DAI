from django import forms
from .models import Cuadro, Galeria

# Cómo crear correctamente los formularios
# https://stackoverflow.com/questions/22739701/django-save-modelform

#
# ───────────────────────────────────────────────────────────────── GALERIAS ─────
#

class CrearGaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = '__all__'




class BorrarGaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ['nombre']


class ActualizarGaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = '__all__' # FIXME ¿campos obligatorios?


#
# ────────────────────────────────────────────────────────────────── CUADROS ─────
#


class CrearCuadroForm(forms.ModelForm):
    #https://docs.djangoproject.com/en/3.2/ref/forms/api/#binding-uploaded-files
    class Meta:
        model = Cuadro
        fields = '__all__'
        widgets = {
            'fecha_creacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }


class BorrarCuadroForm(forms.ModelForm):
    class Meta:
        model = Cuadro
        fields = ['nombre']

class ActualizarGaleriaForm(forms.ModelForm):
    class Meta:
        model = Cuadro
        fields = '__all__' # FIXME