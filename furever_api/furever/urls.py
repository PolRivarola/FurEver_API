from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'animal-adp',AnimalAdopcionView,'animal-adp')
router.register(r'animal-vta',AnimalVentaView,'animal-vta')
router.register(r'interesados',InteresadoView,'interesados')
router.register(r'oferentes',OferenteView,'oferentes')
router.register(r'conexiones',ConexionView,'conexiones')
router.register(r'animales',AnimalAdopcionView,'animales')
router.register(r'documentacion',DocumentacionView,'documentacion')
router.register(r'fotos',FotoView,'fotos')


urlpatterns = [
    path("api/",include(router.urls)),
    path('api/register/interested', InterestedRegistrationView.as_view(), name='interestee-registration'),
    path('api/register/offerer', OffererRegistrationView.as_view(), name='offerer-registration'),
    path('api/login/', LoginView.as_view(), name='login'),

]