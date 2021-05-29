-- Esto es un comentario
-- SQL es un lenguaje de sentencias estructurado en el cual, mediante
-- unas sentencias podemos extraer, agregar, eliminar, actualizar info.
-- de una base de datos
# ESTO es otro comentario
CREATE DATABASE pruebas;
USE pruebas;

CREATE TABLE alumnos(
	# Aqui vendran todas las columnas de esa tabla alumnos
    #solamente puede haber una columna autoincrementable
    id int primary key not null auto_increment,
    nombre varchar(40),
    apellido varchar(25),
    sexo varchar(10),
    numero_emergencia int,
    religion varchar(10),
    fecha_nacimiento date
);

# la forma correcta de ingresar los datos auna tabla es:

INSERT INTO alumnos	(nombre, apellido, sexo, numero_emergencia, religion, fecha_nacimiento)
VALUES				("Eduardo","de rivero","M",974207075,"CATOLICO","1990-08-14");

INSERT INTO alumnos	(nombre, apellido, sexo, numero_emergencia, religion, fecha_nacimiento)
VALUES				("Fiorella","Ccalla","F",948592619,"ATEO","1993-01-07");

INSERT INTO alumnos	(nombre, apellido, sexo, numero_emergencia, religion, fecha_nacimiento)
VALUES				("Matheus","Peña","M",264859,"EVANGELICO","1989-04-06");

INSERT INTO alumnos	(nombre, apellido, sexo, numero_emergencia, religion, fecha_nacimiento)
VALUES				("Aldo","Cotrina Lozano","M",92219087,"CATOLICO","1990-08-14");


SELECT id,nombre FROM alumnos;
#para hacer filtros de busqueda:
#la forma de usar condicionales en base de datos es luego de indicar las tablas que usamos, 
#ponemos la clausula where y luego la columna a hacer la busqueda con su respectivo valor
SELECT * FROM alumnos;

DELETE FROM alumnos WHERE nombre = "Eduardo" and id!= 1;

DELETE FROM alumnos WHERE nombre != "Eduardo";

#SQL_SAFE_UPDATES nos permite hacer funciones "locas", como borrar elementos de la base de datos
#sentencia que habilida/deshabilita el modo seguro que no nos permite hacer eliminaciones
# o actualizaciones en un gran bloque por temor a que cometamos un error garrafal
# 0 = false | 1 => true

SET SQL_SAFE_UPDATES = 1;

SELECT * FROM alumnos;

CREATE TABLE habilidades(
	id int auto_increment not null unique primary key,
    descripcion varchar(100) not null,
    nivel varchar(15)
);

CREATE TABLE habilidades_alumnos(
	id int auto_increment not null unique primary key,
    alumno_id int not null,
    habilidad_id int not null,
    foreign key(habilidad_id) references habilidades (id),
    foreign key(alumno_id) references alumnos (id)
);

