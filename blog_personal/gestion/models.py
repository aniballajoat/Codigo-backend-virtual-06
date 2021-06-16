from datetime import date
from django.utils.timezone import now
from django.db import models

# Create your models here.
class UsuarioModel(models.Model):
    usuarioId = models.AutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_column='id'
    )
    usuarioNombre = models.CharField(
        max_length=25,
        null=False,
        db_column='nombre',
        # a continuacion son parametros para el panel administrativo
        verbose_name='Nombre del usuario', # mostrara para que sirve en el form del panel administrativo
        help_text='Aqui debes ingresar el nombre', # es el campo de ayuda que se formara en el formulario del panel administrativo
    )
    usuarioApellido = models.CharField(
        max_length=25,
        null=False, # indica que el campo no puede no tener un valor (es requerido)
        db_column='apellido',
        verbose_name='Apellido del usuario',
        help_text='Debes ingresar el apellido',
    )
    usuarioCorreo = models.EmailField(
        max_length=50,
        null=False,
        db_column='correo',
        verbose_name='Correo del usuario',
        help_text='Debes ingresar un correo valido'
    )
    usuarioDni = models.CharField(
        max_length = 8,
        null=False,
        db_column='dni',
        verbose_name='Dni del Lector',
        help_text='Ingrese un dni valido'
    )

    class Meta:
        # permite pasar metadatos al padre desde el hijo (setear atributos)
        # modifica el ordenamiento de mis registros de los usuarios
        ordering=['-usuarioCorreo','usuarioNombre']
        # indexacion => indexa cada registro segun una columna o columnas en especifico
        indexes = [models.Index(fields=['usuarioCorreo','usuarioDni'])]
        # modifica el nombre de la tabla en la base de datos
        db_table = 'usuarios'
        # sirve para hacer unica una conjugacion de 2 o mas columnas
        unique_together=[['usuarioCorreo','usuarioDni']]
        # sirve para el panel administrativo es el nombre que se mostrara en vez del nombre de la clase
        verbose_name="usuario"
        # el nombre pero en plural para los registros
        verbose_name_plural="usuarios"

def anio_actual():
    return date.today().year

def opciones_anio():
    return [(anio,anio) for anio in range(1990,date.today().year+1)]

class LibroModel(models.Model):
    libroId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='id'
    )
    libroNombre = models.CharField(
        max_length=45,
        null=False,
        db_column='nombre',
        verbose_name='Nombre del libro',
        help_text='Ingrese un nombre valido'
    )
    libroEdicion = models.IntegerField(
        db_column='edicion',
        choices=opciones_anio(),
        verbose_name='Año edicion',
        help_text='Ingrese el año de la edicion',
        default=anio_actual
    )
    libroAutor = models.TextField(
        db_column='autor',
        null=False,
        verbose_name='Autor del libro',
        help_text='Ingrese el autor'
    )
    libroCantidad = models.IntegerField(
        db_column='cantidad',
        verbose_name='Cantidad',
        default=0,
    )

    def __str__(self):
        return self.libroNombre

    class Meta:
        db_table='libros'
        unique_together=[['libroNombre','libroEdicion', 'libroAutor']]
        verbose_name='libro'
        verbose_name_plural='libros'
        ordering=['-libroEdicion','-libroCantidad','libroNombre']

class PrestamoModel(models.Model):
    prestamoId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='id'
    )
    prestamoFechaInicio = models.DateField(
        default=now,
        db_column='fecha_inicio',
        verbose_name='Fecha de inicio del prestamo'
    )
    prestamoFechaFin = models.DateField(
        db_column='fecha_fin',
        verbose_name='Fecha de fin del prestamo',
        null=False
    )
    prestamoEstado = models.BooleanField(
        default=True,
        db_column='estado',
        verbose_name='Estado del prestamo',
        help_text='Indique el estado del prestamo'
    )
    # opciones para la eliminacion de una PK con relacion
    # CASCADE => se elimina primero la PK y luego las FK's
    # PROTECT => no permite la eliminacion de la PK si tiene relaciones
    # SET_NULL=> elimina la PK y posteriormente todas sus FK cambian de valor a null
    # DO_NOTHING=> elimina la pk y aun mantiene el valor de sus FK (mala integridad)
    # RESTRICT=> no permite la eliminacion como el protect pero lanzara un error de tipo RestrictedError
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#arguments
    # el related_name me servira para poder acceder desde la clase donde se hace la relacion a todas sus llaves foraneas
    usuario = models.ForeignKey(
        to=UsuarioModel,
        db_column='usuario_id',
        on_delete=models.CASCADE,
        related_name='usuarioPrestamos',
        verbose_name='Usuario',
        help_text='Ingrese el nombre del usuario'
    )
    libro = models.ForeignKey(
        to=LibroModel,
        db_column='libro_id',
        on_delete=models.PROTECT,
        related_name='libroPrestamos',
        verbose_name='Libro',
        help_text='Seleccione el libro a prestar'
    )

    class Meta:
        db_table = "prestamos"
        verbose_name="prestamo"
        verbose_name_plural="prestamos"
        ordering=['-prestamoFechaInicio']