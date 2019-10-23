
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from apps.core.api.viewsets import PontoTuristicoViewSet
from apps.atracao.api.viewsets import AtracaoViewSet
from apps.endereco.api.viewsets import EnderecoViewSet
from apps.comentario.api.viewsets import ComentarioViewSet
from apps.avaliacao.api.viewsets import AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, base_name='PontoTuristico')
router.register(r'atracao', AtracaoViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
