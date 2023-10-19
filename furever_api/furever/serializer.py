import re
from rest_framework import serializers
from .models import *
from django.forms.models import model_to_dict


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields = '__all__'

class AnimalAdopcionSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photos')
    interested = serializers.SerializerMethodField('get_interested')
    photo_urls = serializers.ListField(
            child=serializers.CharField(max_length=500),
            write_only=True
        )
    def get_interested(self,animal):
        interested = []
        for i in Conexion.objects.all().filter(animal=animal):
            if i.tipo == "P":
                interested_dict = model_to_dict(i.interesado)
                photo_list = []
                for photo in i.interesado.foto_set.all():
                    photo_list.append(photo.foto)
                interested_dict['photos'] = photo_list
                interested_dict['name'] = i.interesado.user.user.username
                interested_dict['conection'] = i.estado
                
                interested.append(interested_dict)
        return interested
        
    def get_photos(self,animal):
        pics = []
        for i in animal.foto_set.all():
            pattern = r"/file/d/([a-zA-Z0-9_-]+)"
            match = re.search(pattern, i.foto)
            if match:
                file_id = match.group(1)
                pics_dict = {"link": i.foto, "id": file_id}
                pics.append(pics_dict)

        return pics
    
    def create(self, validated_data):
        photo_urls = validated_data.pop('photo_urls', [])
        
        oferente_pk = validated_data.pop('oferente', None)
        
        animal = AnimalAdopcion.objects.create(**validated_data)
        if oferente_pk:
            animal.oferente = oferente_pk
            animal.save()
                

        for url in photo_urls:
            foto = Foto(animal=animal, foto=url)
            foto.save()
        
        return animal
        

    class Meta:
        model = AnimalAdopcion
        fields = ('id',
                  'nombre',
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
                  'oferente',
                  'interested',
                  'photo_urls'
                  )

class AnimalVentaSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField('get_photos')

        
    def get_photos(self,animal):
        pics = []
        for i in animal.foto_set.all():
            pics.append(i.foto)
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
            if i.tipo == "P":
                animal_dict = model_to_dict(i.animal)
                animal_dict['status'] = i.estado
                animal_dict['o_phone'] = i.animal.oferente.user.telefono
                animal_dict['o_name'] = i.animal.oferente.user.user.username
                animal_pic = []
                for photo in Foto.objects.filter(animal=i.animal):
                    pattern = r"/file/d/([a-zA-Z0-9_-]+)"
                    match = re.search(pattern, photo.foto)
                    if match:
                        file_id = match.group(1)
                        animal_pic.append({"link":photo.foto,"id":file_id})
                animal_dict["photos"] = animal_pic
                
                animals.append(animal_dict)
        return animals
    
    def get_name(self,interesee):
        return interesee.user.user.username
    
    def get_photos(self,interesee):
        pics = []
        for i in interesee.foto_set.all():
            pics.append(i.foto)
        return pics
    class Meta:
        model = Interesado
        fields = (
        'name',
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
            animals.append(animal_dict)
        return animals
    
    def get_docs(self,oferente):
        pics = []
        for i in oferente.documentacion_set.all():
            pics.append(i.doc)
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
        
from rest_framework import serializers
from .models import Interesado, User, UserApp

class InteresadoRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    photos = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Interesado
        fields = ['username', 'password', 'phone', 'descripcion', 'ninos', 'tipo_hogar', 'animales_previos', 'animales_actuales', 'horarios','photos']

    def create(self, validated_data):
        # Extract user-related data
        username = validated_data['username']
        password = validated_data['password']
        phone = validated_data['phone']
        photos_data = validated_data.pop('photos', [])

        # Create User and UserApp
        user = User(username=username)
        user.set_password(password)
        user.save()

        user_app = UserApp(user=user, telefono=phone)
        user_app.save()

        # Create Interesado
        interesado_data = validated_data
        interesado_data['user'] = user_app
        del interesado_data['username']
        del interesado_data['password']
        del interesado_data['phone']

        interesado = Interesado.objects.create(**interesado_data)
        for url in photos_data:
            Foto.objects.create(interesado=interesado, foto=url)

        return interesado

class OferenteRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    docs = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Oferente
        fields = ['username', 'password', 'phone', 'provincia', 'empresa_fundacion','docs']

    def create(self, validated_data):
        # Extract user-related data
        username = validated_data['username']
        password = validated_data['password']
        phone = validated_data['phone']
        docs_data = validated_data.pop('docs', [])

        # Create User and UserApp
        user = User(username=username)
        user.set_password(password)
        user.save()

        user_app = UserApp(user=user, telefono=phone)
        user_app.save()

        # Create Interesado
        oferente_data = validated_data
        oferente_data['user'] = user_app
        del oferente_data['username']
        del oferente_data['password']
        del oferente_data['phone']

        oferente = Oferente.objects.create(**oferente_data)
        for url in docs_data:
            Documentacion.objects.create(oferente=oferente, doc=url)

        return oferente

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    

    
