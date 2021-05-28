
from django.db import models
from django.utils import timezone


#sudo docker-compose run web python manage.py makemigrations
#sudo docker-compose run web python manage.py migrate
'''
class Autor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    libro = models.ManyToManyField('Libro', through='Libro')

    def __str__(self):
        return self.nombre
'''


class Libro(models.Model):
  titulo = models.CharField(max_length=200)
  #autor=models.ForeignKey('Autor',on_delete=models.CASCADE)
  #autor = models.ManyToManyField('Autor',related_name='+',through='Autor')
  autor  = models.CharField(max_length=100)
  #autores = models.ManyToManyField(Autor, related_name='book_auths')

  def __str__(self):
    return self.titulo
    
  def form_valid(self, form):
        pass



class Prestamo(models.Model):
  libro   = models.ForeignKey(Libro, on_delete=models.CASCADE)
  fecha   = models.DateField(default=timezone.now)
  usuario = models.CharField(max_length=100)
