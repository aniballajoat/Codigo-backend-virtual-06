from django.urls import path

from .views import (EliminarArchivoController, PlatosController, ArchivosController, CustomPayloadController, RegistroUsuarioController)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
urlpatterns = [
    path('platos', PlatosController.as_view()),
    path('subirImagen', ArchivosController.as_view()),
    path('eliminarImagen', EliminarArchivoController.as_view()),
    path('registro', RegistroUsuarioController.as_view()),
    # Rutas del JWT
    path('login-custom', CustomPayloadController.as_view()),
    path('refresh-token', TokenRefreshView.as_view()),
    path('verify-token', TokenVerifyView.as_view()),
]