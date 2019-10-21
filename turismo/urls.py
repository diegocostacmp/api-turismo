
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from apps.core.api.viewsets import PontoTuristicoViewSet
from apps.atracao.api.viewsets import AtracaoViewSet
from apps.endereco.api.viewsets import EnderecoViewSet
from apps.comentario.api.viewsets import ComentarioViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracao', AtracaoViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'comentario', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
