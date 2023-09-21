from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    nombre = models.CharField("Nombre",max_length=50,null=False,blank=False) 
    especie = models.CharField("Especie",max_length=50,null=False,blank=False) 
    raza = models.CharField("Raza",max_length=50,null=True,blank=True) 
    peso = models.CharField("Nombre",max_length=50,null=False,blank=False)
    descripcion = models.TextField("Descripción",null=True,blank=True)
    fecha_creacion = models.DateField("Fecha creación", auto_now_add=True)


class animalAdopcion(Animal):
    vacunas_completas = models.BooleanField("Vacunas completas",null=False,blank=False)
    edad = models.IntegerField("Edad",null=False)
    necesidades_esp =models.TextField("Necesidades especiales",null=True,blank=True)
    
    def __str__(self):
        return self.nombre


class AnimalVenta(Animal):
    sanidad = models.BooleanField("Sanidad",null=False,blank=False)
    uniformidad = models.BooleanField("Uniformidad",null=False,blank=False)
    trazada = models.BooleanField("Trazada",null=False,blank=False)
    marca_liquida = models.BooleanField("Marca líquida",null=False,blank=False)
    garrapata = models.BooleanField("Garrapata",null=False,blank=False)
    mio_mio = models.BooleanField("Mio Mio",null=False,blank=False)
    precio = models.FloatField("Precio",null=False)
    cantidad = models.IntegerField("Cantidad",null=False)
    
class UserApp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField("Teléfono",null=False)
    def __str__(self):
        return self.nombre
    
class Interesado(models.Model):
    user = models.OneToOneField(UserApp, on_delete=models.CASCADE)
    descripcion = models.TextField("Descripción",null=True,blank=True)
    ninos = models.BooleanField("Niños",null=False,blank=False)
    tipo_hogar = models.TextField("Tipo de hogar",null=True,blank=True)
    animales_previos = models.BooleanField("Animales Previos",null=False,blank=False)
    animales_actuales = models.BooleanField("Animales Actuales",null=False,blank=False)
    horarios = models.TextField("Horarios",null=True,blank=True)

class Oferente(models.Model):
    user = models.OneToOneField(UserApp, on_delete=models.CASCADE)
    provincia = models.CharField("Provincia",max_length=50,null=False,blank=False) 
    empresa_fundacion = models.CharField("Empresa/Fundación",max_length=100,null=False,blank=False) 

class Conexion(models.Model):
    ESTADO_CHOICES = (
    ("EE", "En espera"),
    ("AC", "Aceptado"),
    ("RZ", "Rechazado"),
    )
    estado = models.CharField(choices = ESTADO_CHOICES,max_length=20,default="EE")
    animal = models.OneToOneField(animalAdopcion,on_delete=models.CASCADE)
    interesado = models.OneToOneField(Interesado,on_delete=models.CASCADE)
    oferente = models.OneToOneField(Oferente,on_delete=models.CASCADE)
    fecha_creacion = models.DateField("Fecha creación", auto_now_add=True)

class Foto(models.Model):
    foto = models.FileField(upload_to='user_pics/')
    interesado = models.OneToOneField(Interesado,on_delete=models.CASCADE)
