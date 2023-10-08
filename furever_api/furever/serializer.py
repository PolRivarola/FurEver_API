from rest_framework import serializers
from .models import *
import jsonpickle
from django.forms.models import model_to_dict


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields = '__all__'

class AnimalAdopcionSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photos')
    interested = serializers.SerializerMethodField('get_interested')

    def get_interested(self,animal):
        interested = []
        for i in Conexion.objects.all().filter(animal=animal):
            interested_dict = model_to_dict(i.interested)
            serialized_data = jsonpickle.encode(interested_dict)
            interested.append(serialized_data)
        return interested
        
    def get_photos(self,animal):
        pics = []
        for i in animal.foto_set.all():
            pics.append(i.foto.url)
        return pics

    class Meta:
        model = AnimalAdopcion
        fields = ('nombre',
                  'especie',
                  'raza',
                  'vacunas_completas'
                  ,'edad'
                  ,'necesidades_esp'
                  ,'photos'
                  ,'genero',
                  'peso',
                  'descripcion',
                  'fecha_creacion',
                  'descripcion',
                  'interested'
                  )

class AnimalVentaSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photos')

        
    def get_photos(self,animal):
        pics = []
        for i in animal.foto_set.all():
            pics.append(i.foto.url)
        return pics
    
    class Meta:
        model = AnimalVenta
        fields = ('nombre',
                  'peso',
                  'descripcion',
                  'fecha_creacion',
                  'descripcion',
                  'especie',
                  'raza',
                  'sanidad',
                  'uniformidad',
                  'trazada',
                  'marca_liquida',
                  'garrapata',
                  'mio_mio',
                  'precio',
                  'cantidad',
                  'genero',
                  'photos')


class InteresadoSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photos')
    animals = serializers.SerializerMethodField('get_animals')
    name = serializers.SerializerMethodField('get_name')
    
    def get_animals(self,interesee):
        animals = []
        for i in Conexion.objects.all().filter(interesado=interesee):
            animal_dict = model_to_dict(i.animal)
            serialized_data = jsonpickle.encode(animal_dict)
            animals.append(serialized_data)
        return animals
    
    def get_name(self,interesee):
        return interesee.user.user.username
    
    def get_photos(self,interesee):
        pics = []
        for i in interesee.foto_set.all():
            pics.append(i.foto.url)
        return pics
    class Meta:
        model = Interesado
        fields = (
        'name'
        'descripcion',
        'ninos',
        'tipo_hogar',
        'animales_previos',
        'animales_actuales',
        'horarios',
        'photos',
        'animals'
        )

class OferenteSerializer(serializers.ModelSerializer):
    docs = serializers.SerializerMethodField('get_docs')
    animals = serializers.SerializerMethodField('get_animals')
    name = serializers.SerializerMethodField('get_name')

    def get_name(self,interesee):
        return interesee.user.user.username
    
    def get_animals(self,oferent):
        animals = []
        for i in Animal.objects.all().filter(oferente=oferent):
            animal_dict = model_to_dict(i)
            serialized_data = jsonpickle.encode(animal_dict)
            animals.append(serialized_data)
        return animals
    
    def get_docs(self,oferente):
        pics = []
        for i in oferente.documentacion_set.all():
            pics.append(i.doc.url)
        return pics
    class Meta:
        model = Oferente
        fields = (
        'name',
        'provincia',
        'empresa_fundacion',
        'docs',
        'animals',
        
        
        
        )

class ConexionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conexion
        fields = '__all__'
        
class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'

class DocumentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentacion
        fields = '__all__'