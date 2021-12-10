from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('test_template', views.test_template, name="test_template")
    path('crear_cuadro', views.crear_cuadro, name='index'),
    path('crear_galeria', views.crear_galeria, name='index'),
    path('borrar_galeria', views.borrar_galeria, name='index'),
    path('borrar_cuadro', views.borrar_cuadro, name='index'),
    path('actualizar_galeria/<int:pk>', views.actualizar_galeria, name='index'),
    path('actualizar_cuadro/<int:pk>', views.actualizar_cuadro, name='index'),
    path('formulario_edit_galeria', views.formulario_edit_galeria, name='index'),
    path('formulario_edit_cuadro', views.formulario_edit_cuadro, name='index'),
]