DROP DATABASE IF EXISTS EMPRESA;
CREATE DATABASE IF NOT EXISTS EMPRESA;
USE EMPRESA;

CREATE TABLE IF NOT EXISTS departamentos(
	id int not null unique primary key auto_increment,
    nombre varchar(50),
    piso int
);

CREATE TABLE IF NOT EXISTS personales(
	id int not null unique primary key auto_increment,
    nombre varchar(50),
    apellido varchar(50),
    identificador text,
    departamento_id int,
    supervisor_id int,
    constraint departamentos_personales foreign key (departamento_id) references departamentos(id),
    constraint personales_personales foreign key (supervisor_id) references personales (id)
);

INSERT INTO departamentos 	(nombre,piso)
VALUES
('Ventas',1),
('Administracion',2),
('Finanzas',2),
('Marketing',3);
                            
SELECT * 
FROM departamentos;