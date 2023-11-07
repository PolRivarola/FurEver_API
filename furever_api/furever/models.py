from django.db import models
from django.contrib.auth.models import User
 

class UserApp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField("Teléfono",null=False)
    def __str__(self):
        return self.user.username

    

class Oferente(models.Model):
    user = models.OneToOneField(UserApp, on_delete=models.CASCADE)
    provincia = models.CharField("Provincia",max_length=50,null=True,blank=True) 
    empresa_fundacion = models.CharField("Empresa/Fundación",max_length=100,null=True,blank=True) 
    def __str__(self):
        return self.user.user.username
    

class Interesado(models.Model):
    user = models.OneToOneField(UserApp, on_delete=models.CASCADE)
    descripcion = models.TextField("Descripción",null=True,blank=True)
    ninos = models.BooleanField("Niños",null=True,blank=True)
    tipo_hogar = models.TextField("Tipo de hogar",null=True,blank=True)
    animales_previos = models.BooleanField("Animales Previos",null=True,blank=True)
    animales_actuales = models.BooleanField("Animales Actuales",null=True,blank=True)
    horarios = models.TextField("Horarios",null=True,blank=True)
    
    def __str__(self):
        return self.user.user.username
    
class Animal(models.Model):
    GENERO_CHOICES = (
    ("M", "Macho"),
    ("H", "Hembra"),
    )
    nombre = models.CharField("Nombre",max_length=50,null=False,blank=False)
    genero = models.CharField(choices = GENERO_CHOICES,max_length=20,default="P")
    peso = models.CharField("Peso",max_length=50,null=False,blank=False)
    descripcion = models.TextField("Descripción",null=True,blank=True)
    fecha_creacion = models.DateField("Fecha creación", auto_now_add=True)
    oferente = models.ForeignKey(Oferente,on_delete=models.CASCADE,default=None,null=True,blank=True)
    
    def __str__(self):
        return self.nombre

class AnimalAdopcion(Animal):
    ESPECIE_CHOICES = (
    ("P", "Perro"),
    ("G", "Gato"),
    ("C", "Conejo"),
    ("T","Tortuga"),
    ("S","Serpiente"),
    ("DG","De granja"),
    ("O","Otros")
    )
    
    especie = models.CharField(choices = ESPECIE_CHOICES,max_length=20,default="P")
    raza = models.CharField("Raza",max_length=50,null=True,blank=True) 
    vacunas_completas = models.BooleanField("Vacunas completas",null=False,blank=False)
    edad = models.IntegerField("Edad",null=False)
    necesidades_esp =models.TextField("Necesidades especiales",null=True,blank=True)
    
    def __str__(self):
        return self.nombre


class AnimalVenta(Animal):
    ESPECIE_CHOICES = (
    ("V", "Vaca"),
    ("G", "Gallina"),
    ("C", "Cerdo"),
    ("C","Caballos"),
    ("O","Otros")
    )
    
    especie = models.CharField(choices = ESPECIE_CHOICES,max_length=20,default="P")
    raza = models.CharField("Raza",max_length=50,null=True,blank=True) 
    sanidad = models.BooleanField("Sanidad",null=False,blank=False,default=False)
    uniformidad = models.BooleanField("Uniformidad",null=False,blank=False,default=False)
    trazada = models.BooleanField("Trazada",null=False,blank=False,default=False)
    marca_liquida = models.BooleanField("Marca líquida",null=False,blank=False,default=False)
    garrapata = models.BooleanField("Garrapata",null=False,blank=False,default=False)
    mio_mio = models.BooleanField("Mio Mio",null=False,blank=False,default=False)
    precio = models.FloatField("Precio",null=False,default=False)
    cantidad = models.IntegerField("Cantidad",null=False,default=False)
    

class Conexion(models.Model):
    ESTADO_CHOICES = (
    ("EE", "En espera"),
    ("AC", "Aceptado"),
    ("RZ", "Rechazado"),
    )
    
    TIPO_CHOICES = (
        ("P","Positiva"),
        ("N","Negativa"),
    )
    estado = models.CharField(choices = ESTADO_CHOICES,max_length=20,default="EE")
    animal = models.ForeignKey(AnimalAdopcion,on_delete=models.CASCADE)
    interesado = models.ForeignKey(Interesado,on_delete=models.CASCADE)
    fecha_creacion = models.DateField("Fecha creación", auto_now_add=True)
    tipo = models.CharField(choices = TIPO_CHOICES,max_length=20,default="P")
    def __str__(self):
        return self.animal.nombre +"+"+self.interesado.user.user.username
    
class Foto(models.Model):
    foto = models.CharField("Link a foto",max_length=500,null=True,blank=True)
    interesado = models.ForeignKey(Interesado,on_delete=models.CASCADE,null=True,blank=True)
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        if self.animal:
            show = self.animal.nombre
        else:
            show = self.interesado.user.user.username
        return "Foto de "+ show

class Documentacion(models.Model):
    doc = models.CharField("Link a documentacion",max_length=500,null=True,blank=True)
    oferente = models.ForeignKey(Oferente,on_delete=models.CASCADE)
    descripcion = models.TextField("Descripción",null=True,blank=True)
    
    def __str__(self):

        return "Foto de "+ self.oferente.user.user.username

 