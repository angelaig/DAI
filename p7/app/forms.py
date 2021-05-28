from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.layout import Submit
from django.forms import ModelForm

from .models import *

from django import forms
from app.models import *
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm


#https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html
class LibroForm(forms.ModelForm):
    '''
    class Meta:
        model = Libro
        fields = ['titulo', 'autor']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save libro'))

    def get_form(self, form_class=None):
       form = super().get_form(form_class)
       form.helper = FormHelper()
       form.helper.add_input(Submit('submit', 'Create', css_class='btn-primary'))
       return form
    
    def send_libro(self):
        pass
    '''
    class Meta:
        model = Libro
        fields = ['titulo', 'autor']
        
    
    def registrar(self):
        nlibro = Libro(titulo = self.data['titulo'],
                        autor = self.data['autor'],
                        )
        nlibro.save()
        return 'Correcto registro'

class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'fecha']
        

    fecha = forms.DateField(widget=forms.SelectDateWidget(years=range(2000,2021)))
    
    def registrar(self, user):
        fecha = datetime(int(self.data['fecha_year']),
                        int(self.data['fecha_month']),
                        int(self.data['fecha_day']))
        nprestamo = Prestamo(libro=self.instance.libro,
                        fecha=fecha,
                        usuario=user)
        nprestamo.save()
        return 'Correcto registro'




class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', "password1", "password2", 'is_staff']

