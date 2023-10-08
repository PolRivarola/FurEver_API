from rest_framework import serializers
from .models import *

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields = '__all__'

class AnimalAdopcionSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photos')
    
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
                  )

class AnimalVentaSerializer(serializers.ModelSerializer):
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
                  'genero',)


class InteresadoSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photos')
    
    def get_photos(self,animal):
        pics = []
        for i in animal.foto_set.all():
            pics.append(i.foto.url)
        return pics
    class Meta:
        model = Interesado
        fields = (
        'descripcion',
        'ninos',
        'tipo_hogar',
        'animales_previos',
        'animales_actuales',
        'horarios',
        'photos'
        )

class OferenteSerializer(serializers.ModelSerializer):
    docs = serializers.SerializerMethodField('get_photos')
    
    def get_docs(self,oferente):
        pics = []
        for i in oferente.documentacion_set.all():
            pics.append(i.doc.url)
        return pics
    class Meta:
        model = Oferente
        fields = (
        'descripcion',
        'ninos',
        'tipo_hogar',
        'animales_previos',
        'animales_actuales',
        'horarios',
        'docs'
        
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