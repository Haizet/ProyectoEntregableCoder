from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nac = models.DateField()
    
    def get_class(self):
        class_name = 'Familiar'
        return class_name

class Hijo(Familiar):
    es_hijo = models.BooleanField()
        
    def get_class(self):
        class_name = 'Hijo'
        return class_name

class Padres(Familiar):
    es_padre = models.BooleanField()

    def get_class(self):
        class_name = 'Padre'
        return class_name