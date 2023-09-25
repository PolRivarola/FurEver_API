from rest_framework import viewsets
from .serializer import *
from .models import *

class AnimalView(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

class AnimalAdopcionView(viewsets.ModelViewSet):
    serializer_class = AnimalAdopcionSerializer
    queryset = AnimalAdopcion.objects.all()

class AnimalVentaView(viewsets.ModelViewSet):
    serializer_class = AnimalVentaSerializer
    queryset = AnimalVenta.objects.all()

class InteresadoView(viewsets.ModelViewSet):
    serializer_class = InteresadoSerializer
    queryset = Interesado.objects.all()

class OferenteView(viewsets.ModelViewSet):
    serializer_class = OferenteSerializer
    queryset = Oferente.objects.all()

class ConexionView(viewsets.ModelViewSet):
    serializer_class = ConexionSerializer
    queryset = Conexion.objects.all()

class DocumentacionView(viewsets.ModelViewSet):
    serializer_class = DocumentacionSerializer
    queryset = Documentacion.objects.all()

class FotoView(viewsets.ModelViewSet):
    serializer_class = FotoSerializer
    queryset = Foto.objects.all()
