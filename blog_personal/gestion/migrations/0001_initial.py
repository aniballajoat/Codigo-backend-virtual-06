# Generated by Django 3.2.4 on 2021-06-16 01:21

from django.db import migrations, models
import gestion.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibroModel',
            fields=[
                ('libroId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('libroNombre', models.CharField(db_column='nombre', help_text='Ingrese un nombre valido', max_length=45, verbose_name='Nombre del libro')),
                ('libroEdicion', models.IntegerField(choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], db_column='edicion', default=gestion.models.anio_actual, help_text='Ingrese el año de la edicion', verbose_name='Año edicion')),
                ('libroAutor', models.TextField(db_column='autor', help_text='Ingrese el autor', verbose_name='Autor del libro')),
                ('libroCantidad', models.IntegerField(db_column='cantidad', default=0, verbose_name='Cantidad')),
            ],
            options={
                'verbose_name': 'libro',
                'verbose_name_plural': 'libros',
                'db_table': 'libros',
                'ordering': ['-libroEdicion', '-libroCantidad', 'libroNombre'],
            },
        ),
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('usuarioId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('usuarioNombre', models.CharField(db_column='nombre', help_text='Aqui debes ingresar el nombre', max_length=25, verbose_name='Nombre del usuario')),
                ('usuarioApellido', models.CharField(db_column='apellido', help_text='Debes ingresar el apellido', max_length=25, verbose_name='Apellido del usuario')),
                ('usuarioCorreo', models.EmailField(db_column='correo', help_text='Debes ingresar un correo valido', max_length=50, verbose_name='Correo del usuario')),
                ('usuarioDni', models.CharField(db_column='dni', help_text='Ingrese un dni valido', max_length=8, verbose_name='Dni del Lector')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'db_table': 'usuarios',
                'ordering': ['-usuarioCorreo', 'usuarioNombre'],
            },
        ),
        migrations.AddIndex(
            model_name='usuariomodel',
            index=models.Index(fields=['usuarioCorreo', 'usuarioDni'], name='usuarios_correo_fd9ad5_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='usuariomodel',
            unique_together={('usuarioCorreo', 'usuarioDni')},
        ),
        migrations.AlterUniqueTogether(
            name='libromodel',
            unique_together={('libroNombre', 'libroEdicion', 'libroAutor')},
        ),
    ]
