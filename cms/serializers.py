from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import *
from rest_framework import serializers
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings


class PlatoSerializer(serializers.ModelSerializer):
    platoFoto = serializers.CharField(max_length=100)
    class Meta:
        model = PlatoModel
        fields = '__all__'


class ArchivoSerializer(serializers.Serializer):
    # max_length => indica el tamaño maximo del nombre del archivo
    # use_url => si es True, entonces el valor de la URL sera usado para mostrar la ubicacion del archivo, si es False entonces se usara el nombre del archivo para su representacion, su valor por defecto es UPLOADED_FILES_USE_URL que significa True en la configuracion interna de DRF
    archivo = serializers.ImageField(max_length=20, use_url=True)

    def save(self):
        archivo: InMemoryUploadedFile = self.validated_data.get('archivo')
        # para ver el tipo de archivo que es
        #print(archivo.content_type)
        # para ver el nombre del archivo
        #print(archivo.name)
        # para ver el tamaño del archivo en bytes
        #print(archivo.size)
        # para leer el archivo, una vez que se lee el archivo se elimina su informacion
        # archivo.read()

        ruta = default_storage.save(
            archivo.name, ContentFile(archivo.read()))
        return settings.MEDIA_URL + ruta
        # ruta_final = path.join(settings.MEDIA_ROOT, ruta)
        #print(ruta)
        #print(ruta_final)


class EliminarArchivoSerializer(serializers.Serializer):
    nombre = serializers.CharField()

class CustomPayloadSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super(CustomPayloadSerializer,cls).get_token(user)
        token['usuarioTipo'] = user.usuarioTipo
        token['mensaje'] = 'Holis'
        return token
class RegistroUsuarioSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    def save(self):
        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioApellido = self.validated_data.get('usuarioApellido')
        usuarioCorreo = self.validated_data.get('usuarioCorreo')
        usuarioTipo = self.validated_data.get('usuarioTipo')
        usuarioTelefono = self.validated_data.get('usuarioTelefono')
        password = self.validated_data.get('password')
        nuevoUsuario = UsuarioModel(
            usuarioNombre=usuarioNombre,
            usuarioCorreo=usuarioCorreo,
            usuarioApellido=usuarioApellido,
            usuarioTipo=usuarioTipo,
            usuarioTelefono=usuarioTelefono,
        )
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = UsuarioModel
        exclude = ['groups', 'user_permissions']
        # es para dar configuracion adicional a los atributos de un model serializer, usando el atributo extra_kwargs se puede
        # editar la configuracion de sis olo escritura, solo lectura, required, allow null, default y error messages
        # no es necesario volver a declarar las mismas configuraciones iniciales ()
        extra_kwargs = {
            'password':{
                'write_only': True
            }
        }