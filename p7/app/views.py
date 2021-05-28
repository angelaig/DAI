from django.shortcuts import render, HttpResponse,redirect
from django.views.generic import CreateView,UpdateView


from .models import Libro
from .forms import *
from dataclasses import dataclass, field

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# mi_aplicacion/views.py


# Create your views here.

def home(request):
     return render(request,'base.html')

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)

@login_required
def libros(request):
    items = Libro.objects.all()  # Aquí van la las variables para la plantilla
    return render(request,'lista_libros.html', {'items': items })

@staff_member_required(login_url='accounts/login/')
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

@staff_member_required
def borrarLibro(request, item_id):
    instance = Libro.objects.get(pk=item_id)
    instance.delete()
    return redirect(libros)



@staff_member_required
def crearLibro(request):
    if request.method == 'POST':
        register_form = LibroForm(request.POST)
        if register_form.is_valid():
            success = register_form.registrar()
            return redirect(libros)
    else:
        nuevoLibro = LibroForm()
        return render(request,'nuevo_libro.html', {'register_form': nuevoLibro})

@login_required
def crearPrestamo(request):
    error=None
    if request.method == 'POST':
        register_form = PrestamoForm(request.POST)
        if register_form.is_valid():
            print("valido")
            success = register_form.registrar(user=request.user)
            #register_form.save()
            return redirect('Prestamos')
        else:
            error=register_form.errors
    else:
        register_form = PrestamoForm()
    return render(request,'nuevo_Prestamo.html', {'form': register_form,'error': error})


@login_required
def Prestamos(request):
    items = Prestamo.objects.all().order_by('fecha')
    return render(request,'lista_Prestamos.html', {'items': items })

@login_required
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

@login_required
def borrarPrestamo(request, item_id):
    instance = Prestamo.objects.get(pk=item_id)
    if request.method=='POST':
        instance.delete()
        return redirect('Prestamos')
    return render(request,'borrar_Prestamo.html',{'instance': instance})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            rpassword = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=rpassword)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

def staff(request):
    return render(request, 'staff.html')
