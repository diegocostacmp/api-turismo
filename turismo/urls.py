
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from apps.core.api.viewsets import PontoTuristicoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
