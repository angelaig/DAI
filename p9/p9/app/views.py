from django.shortcuts import render, HttpResponse,redirect
from django.views.generic import CreateView,UpdateView


from .models import Libro
from .forms import *
from dataclasses import dataclass, field
# mi_aplicacion/views.py


# Create your views here.

def index(request):
     return render(request,'base.html')

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)

def libros(request):
    items = Libro.objects.all()  # Aquí van la las variables para la plantilla
    return render(request,'lista_libros.html', {'items': items })


def editarLibro(request, item_id):
    instancia = Libro.objects.get(pk=item_id)

    form = LibroForm(instance=instancia)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
        return redirect(libros)

    return render(request,'editar_libro.html', {'register_form': form, 'item_id':item_id})

def borrarLibro(request, item_id):
    instance = Libro.objects.get(pk=item_id)
    instance.delete()
    return redirect(libros)

def crearLibro(request):
    if request.method == 'POST':
        register_form = LibroForm(request.POST)
        if register_form.is_valid():
            success = register_form.registrar()
            return redirect(libros)
    else:
        nuevoLibro = LibroForm()
        return render(request,'nuevo_libro.html', {'register_form': nuevoLibro})


def crearPrestamo(request):
    error=None
    if request.method == 'POST':
        register_form = PrestamoForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('Prestamos')
        else:
            error=register_form.errors
    else:
        register_form = PrestamoForm()
    return render(request,'nuevo_Prestamo.html', {'form': register_form,'error': error})

def Prestamos(request):
    items = Prestamo.objects.all().order_by('fecha')
    return render(request,'lista_Prestamos.html', {'items': items })

def editarPrestamo(request, item_id):
    error=None
    instancia = Prestamo.objects.get(pk=item_id)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('Prestamos')
        else:
            error=form.errors
    else:
        form = PrestamoForm(instance=instancia)
    
    return render(request,'editar_Prestamo.html', {'form': form, 'item_id':item_id, 'error': error})

def borrarPrestamo(request, item_id):
    instance = Prestamo.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('Prestamos')
    return render(request,'borrar_Prestamo.html',{'instance': instance})
