from rest_framework import serializers
from .models import *

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields = '__all__'

class AnimalAdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalAdopcion
        fields = '__all__'

class AnimalVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalVenta
        fields = '__all__'


class InteresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interesado
        fields = '__all__'

class OferenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferente
        fields = '__all__'

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
        model = Foto
        fields = '__all__'