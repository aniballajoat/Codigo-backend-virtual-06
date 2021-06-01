CREATE DATABASE ZAPATERIA;

USE ZAPATERIA;

CREATE TABLE categorias(
	id int not null unique auto_increment,
    nombre varchar(50),
    abbr varchar(10),
    imagen text
);

CREATE TABLE productos(
	id int not null unique auto_increment,
    nombre varchar(50),
    precio decimal (5,2),
    disponible boolean,
    categoria_id int,
    #constraint sirve para modificar el nombre con el cual se creara la relacion entre
    #la tabla categorai y la tabla producto, el valor por defecto es:
    #categorias_productos_ibfk_n => n es el numero de creacion de la constraint
    #ibfk=> innodb foreign key
    constraint relacion_producto_categoria
    foreign key (categoria_id) references categorias (id)
);


INSERT INTO categorias 	(nombre, abbr, imagen) VALUE
						("ZAPATO","ZAP","url1"),
                        ("ZAPATILLA","ZAPT","url2"),
                        ("BOTIN","BOT","url3"),
                        ("BOTA","BOTA","url4");
                        
INSERT INTO PRODUCTOS 	(nombre, precio, disponible, categoria_id) VALUES
						("ZAPATO VERANO",99.90,true,1),
                        ("ZAPATO HOMBRE",120.00,true,1),
                        ("ZAPATO MUJER",199.00,false,1),
                        ("ZAPATILLA TREKKIN HOMBRE",189.90,true,2),
                        ("ZAPATILLA RUN MUJER",200.00,true,2),
                        ("ZAPATILLA OFFROAD MUJER",320.89,true,2),
                        ("BOTIN TACO 4",520.00,true,3),
                        ("BOTA TACO 10",710,false,4);
                        
                        
-- SELECT * from categorias WHERE nombre LIKE '%A%';
-- SELECT * from productos WHERE precio >=100;

INSERT INTO CATEGORIAS 	(nombre, abbr, imagen) value
						("BEBES","BEB","url5");
                        
INSERT INTO PRODUCTOS 	(nombre, precio, disponible) VALUES
						("SANDALIAS BOB TORONJA",19.90,true);
SELECT * FROM CATEGORIAS;
SELECT * FROM CATEGORIAS INNER JOIN PRODUCTOS ON CATEGORIAS.ID = PRODUCTOS.CATEGORIA_ID;

SELECT * FROM CATEGORIAS LEFT JOIN PRODUCTOS ON CATEGORIAS.ID = PRODUCTOS.CATEGORIA_ID;

SELECT * FROM CATEGORIAS RIGHT JOIN PRODUCTOS ON CATEGORIAS.ID = PRODUCTOS.CATEGORIA_ID;
-- AGGREGATION FUNCTIONS
SELECT count(*) from productos;
SELECT count(*) from categorias;

-- seleccioname todos los nombres cuyo alias sera el nombre del producto, precio y disponible de
-- categorias, interseccion producto cuando cat.id = prod.categoria_id donde el nombre de la categoria
-- sea zapato

-- ALIAS =>AS
SELECT cat.nombre as 'nombre del producto', prod.precio, prod.disponible
FROM CATEGORIAS AS cat JOIN PRODUCTOS as prod ON cat.ID = prod.CATEGORIA_ID
WHERE cat.nombre = "ZAPATO";

