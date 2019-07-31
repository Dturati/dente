app_name = 'app'
from django.urls import path, include
from rest_framework import routers
from upload.api.viewsets import processa_dente
from upload.api.viewsets import upload

# router = routers.DefaultRouter()
# router.register(r'dente', processa_dente)
urlpatterns = [
    path(r'dentes/', processa_dente),
    path(r'dentes/up', upload)
]