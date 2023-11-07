from rest_framework import viewsets
from .serializer import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import requests
from django.contrib.auth import authenticate, login



class AnimalView(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

class AnimalAdopcionView(viewsets.ModelViewSet):
    serializer_class = AnimalAdopcionSerializer
    model = AnimalAdopcion
    
    def get_queryset(self):
        fields = [f.column for f in self.model._meta.fields]
        fdict = {k: self.request.GET.get(k) for k in self.request.GET
                 }
        interested = fdict.pop('interested', None)
        especie = fdict.pop('especie', None)
        oferente_name = fdict.pop('owner', None)
        queryset = self.model.objects.filter(**fdict)
        if oferente_name:
            queryset = queryset.filter(oferente__user__user__username=oferente_name)
        if interested:
            queryset = queryset.exclude(conexion__interesado__pk = interested)
            queryset = queryset.exclude(conexion__estado = "AC")
        if especie:
            if especie != "":
                    queryset = queryset.filter(especie=especie)
        return queryset
    
    def update(self, request, *args, **kwargs):
        
        animal = AnimalAdopcion.objects.filter(pk=request.data.get("pk")).first()
        if animal:
            photos_data = request.data.get("photo_urls")
            Foto.objects.filter(animal=animal).delete()
            for url in photos_data:
                Foto.objects.create(animal=animal, foto=url)

            super().update(request, *args, **kwargs)
            return Response({'message': 'Animal actualizado con éxito'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Hubo un error actualizando al animal'}, status=status.HTTP_400_BAD_REQUEST)


class AnimalVentaView(viewsets.ModelViewSet):
    serializer_class = AnimalVentaSerializer
    model=AnimalVenta
    
    def get_queryset(self):
        fields = [f.column for f in self.model._meta.fields]
        fdict = {k: self.request.GET.get(k) for k in self.request.GET
                 }
        interesado_name = fdict.pop('owner', None)
        queryset = self.model.objects.filter(**fdict)
        if interesado_name:
            queryset = queryset.filter(oferente__user__user__username=interesado_name)
        return queryset

class InteresadoView(viewsets.ModelViewSet):
    serializer_class = InteresadoSerializer
    model = Interesado
    def get_queryset(self):
        fdict = {k: self.request.GET.get(k) for k in self.request.GET
                 }
        interesado_name = fdict.pop('name', None)
        queryset = self.model.objects.filter(**fdict)
        if interesado_name:
            queryset = queryset.filter(user__user__username=interesado_name)
        return queryset
    
    def update(self, request, *args, **kwargs):
        
        interested = Interesado.objects.filter(pk=request.data.get("pk")).first()
        if interested:
            phone = request.data.get("phone")
            photos_data = request.data.get("photos")
            password = request.data.get("password")
            if password != '':
                interested.user.user.set_password(password)
                interested.user.user.save()
            interested.user.telefono = phone
            interested.user.save()
            Foto.objects.filter(interesado=interested).delete()
            for url in photos_data:
                Foto.objects.create(interesado=interested, foto=url)

            super().update(request, *args, **kwargs)
            return Response({'message': 'User actualizado con éxito'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Hubo un error actualizando el usuario'}, status=status.HTTP_400_BAD_REQUEST)

class OferenteView(viewsets.ModelViewSet):
    serializer_class = OferenteSerializer
    model = Oferente
    def get_queryset(self):
        fdict = {k: self.request.GET.get(k) for k in self.request.GET
                }
        oferente_name = fdict.pop('name', None)
        queryset = self.model.objects.filter(**fdict)
        if oferente_name:
            queryset = queryset.filter(user__user__username=oferente_name)
        return queryset
    
    def update(self, request, *args, **kwargs):
        
        offerer = Oferente.objects.filter(pk=request.data.get("pk")).first()
        if offerer:
            phone = request.data.get("phone")
            docs = request.data.get("docs")
            password = request.data.get("password")
            if password != "":
                offerer.user.user.set_password(password)
                offerer.user.user.save()
            offerer.user.telefono = phone
            offerer.user.save()
            Documentacion.objects.filter(oferente=offerer).delete()
            for url in docs:
                Documentacion.objects.create(oferente=offerer, doc=url)

            super().update(request, *args, **kwargs)
            return Response({'message': 'User actualizado con éxito'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Hubo un error actualizando el usuario'}, status=status.HTTP_400_BAD_REQUEST)


class ConexionView(viewsets.ModelViewSet):
    serializer_class = ConexionSerializer
    queryset = Conexion.objects.all()

class DocumentacionView(viewsets.ModelViewSet):
    serializer_class = DocumentacionSerializer
    queryset = Documentacion.objects.all()

class FotoView(viewsets.ModelViewSet):
    serializer_class = FotoSerializer
    queryset = Foto.objects.all()

class InterestedRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = InteresadoRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            interestee = serializer.save()
            return Response({'message': 'User registrado con éxito'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
        
    
class OffererRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OferenteRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            offerer = serializer.save()
            return Response({'message': 'User registrado con éxito'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DismissConnectionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        interested = request.data['interested']
        animal = request.data['animal']

        conection = Conexion.objects.filter(interesado=interested,animal=animal).first()

        if conection:
            conection.estado = "N"
            conection.save()
            return Response({'message': 'Se cancelo la conexión'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Hubo un error en la cancelación de conexión'}, status=status.HTTP_400_BAD_REQUEST)

class ConectionDecisionView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        interested = request.data['interested']
        animal = request.data['animal']
        answer = request.data['answer']
        
        conection = Conexion.objects.filter(interesado=interested,animal=animal).first()
        if conection:
            if answer == "accept":
                conection.estado = "AC"
                for conection_r in Conexion.objects.filter(animal=animal):
                    if conection_r.interesado != interested:
                        conection_r.estado = "RZ"
                        conection_r.save()
            if answer == "reject":
                conection.estado = "RZ"
            conection.save()
            return Response({'message': 'Se cambio el estado de la conexión'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No se encontro conexión'}, status=status.HTTP_400_BAD_REQUEST)

class CardDecisionView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        interested = request.data['interested']
        animal = request.data['animal']
        c_type = request.data['type']
        
        try:
            if not Conexion.objects.filter(
                animal = AnimalAdopcion.objects.get(pk=animal),
                interesado = Interesado.objects.get(pk=interested)):
                Conexion.objects.create(
                tipo=c_type,
                animal = AnimalAdopcion.objects.get(pk=animal),
                interesado = Interesado.objects.get(pk=interested)
                )
            
            return Response({'message': 'Se creó la conexión'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': 'Error:'+ str(e)}, status=status.HTTP_400_BAD_REQUEST)

  

class LoginView(APIView):
    def post(self, request):
        print(request.data)
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                if Interesado.objects.filter(user__user__username = username).first():
                    u_type = "Interested"
                    user = Interesado.objects.filter(user__user__username = username).first()
                else:
                    u_type = "Offerer"
                    user = Oferente.objects.filter(user__user__username = username).first()
                    
                
                user_data = {
                    'id':user.id,
                    'password':password,
                    'username':username,
                    'tipo': u_type
                }
                return Response({'message': 'Login successful', 'user_data': user_data}, status=status.HTTP_200_OK)
        
        return Response({'message': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)

def test_user_registration():
    url = 'http://localhost:8000/furever/api/register/'  # Replace with your API endpoint URL
    data = {
        'username': 'testuser4',
        'password': 'testpassword',
        'phone': '1234',
        'descripcion': 'Lorem',
        'ninos': False,  # Use True instead of 'True'
        'tipo_hogar': "Lorem",
        'animales_previos': False,  # Use True instead of 'True'
        'animales_actuales': True,  # Use True instead of 'True'
        'horarios': "Lorem",
        'photos': ['url1', 'url2', 'url3'],
    }

    headers = {'Content-Type': 'application/json'}  # Set the Content-Type header
    response = requests.post(url, json=data, headers=headers)  # Use json=data to send JSON content
    
    
    print("Response Status Code:", response.status_code)

    # Print response content
    print("Response Content:")
    print(response.text)

    # Print response headers
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

    # Check if there's a specific error message in the response
    if 'detail' in response.json():
        error_message = response.json()['detail']
        print("Error Message:", error_message)

    assert response.status_code == 201

def test_login():
    url = 'http://localhost:8000/furever/api/login/'  # Replace with your API endpoint URL
    data = {
        'username': 'testuser',
        'password': 'testpassword',
    }

    response = requests.post(url, json=data)
    print(response)
    assert response.status_code == 200

# test_login()