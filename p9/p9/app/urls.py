from django.urls import path
from . import views

urlpatterns = [
  path('', views.libros, name='index'),
  path('test_template', views.test_template, name='test_template'),
  path('lista_libros', views.libros, name='libros'),
  path('crearLibro', views.crearLibro, name='crearLibro'),
  path('borrarLibro/<item_id>', views.borrarLibro, name='borrarLibro'),
  path('editarLibro/<item_id>', views.editarLibro, name='editarLibro'),

  path('Prestamos', views.Prestamos, name='Prestamos'),
  path('crearPrestamo', views.crearPrestamo, name='crearPrestamo'),
  path('editarPrestamo/<item_id>', views.editarPrestamo, name='editarPrestamo'),
  path('borrarPrestamo/<item_id>', views.borrarPrestamo, name='borrarPrestamo'),
]


