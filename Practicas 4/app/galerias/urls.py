from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('test_template', views.test_template, name="test_template")
    path('crear_cuadro', views.crear_cuadro, name='index'),
    path('crear_galeria', views.crear_galeria, name='index')
]