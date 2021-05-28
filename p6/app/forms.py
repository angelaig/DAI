from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.layout import Submit
from django.forms import ModelForm

from .models import Libro,Prestamo
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
        nuevo_libro = Libro(titulo = self.data['titulo'],
                        autor = self.data['autor'],
                        )
        nuevo_libro.save()
        return 'Registro exitoso'

class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'