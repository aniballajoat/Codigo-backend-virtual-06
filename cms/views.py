from .models import PlatoModel
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView)
from .serializers import *
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.conf import settings
import os


class ArchivosController(CreateAPIView):
    serializer_class = ArchivoSerializer

    def post(self, request: Request):

        data = self.serializer_class(data=request.FILES)
        if data.is_valid():
            url = request.META.get('HTTP_HOST')
            archivo = data.save()
            return Response(data=
            {
                "success": True,
                "content": url+archivo,
                "message": "Archivo subido exitosamente"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "success": False,
                "content": data.errors,
                "message": "Error al subir el archivo"
            })
        # return Response('ok')


class PlatosController(ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer

    def post(self, request: Request):
        # para ver que archivos me esta mandando el frontend
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data={
                "success": True,
                "content": data.data,
                "message": "Creacion de plato exitosa"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "content": data.errors,
                "success": False,
                "message": "Error al crear el plato"
            }, status=status.HTTP_400_BAD_REQUEST)

class EliminarArchivoController(DestroyAPIView):
    serializer_class=EliminarArchivoSerializer
    def delete(self,request:Request):
        data=self.serializer_class(data=request.data)
        try:
            if data.is_valid():
                os.remove(settings.MEDIA_ROOT / 
                            data.validated_data.get('nombre'))
                return Response(data={
                    "success": True,
                    "content":None,
                    "message":"Imagen eliminada exitosamente"
                })
            else:
                return Response(data={
                    "success": False,
                    "content":data.errors,
                    "message":"Error al eliminar la imagen"
            }, status=os.stat)
        except:
            return Response(data={
                "success": False,
                "content":None,
                "message":"Imagen ya fue eliminada previamente"
            })
class CustomPayloadController(TokenObtainPairView):
    # sirve para modificar el payload de la token de acceso
    permission_classes = [AllowAny]
    serializer_class = CustomPayloadSerializer

class RegistroUsuarioController(CreateAPIView):
    serializer_class = RegistroUsuarioSerializer
    def post(self, request:Request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response({
                "message": "Usuario Creado exitosamente",
                "content": data.data,
                "success": True
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "Error al crear usuario",
                "content": data.errors,
                "success": False
            })