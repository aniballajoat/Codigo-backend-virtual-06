#from datetime import datetime

# pip install faker
from faker import Faker
fake = Faker()


def data_personales(limite):
    for id in range(1, limite+1):
        nombre = fake.first_name()
        apellido = fake.last_name()
        correo = fake.email()
        dni = fake.random_int(min=10000000, max=99999999)
        print('INSERT INTO usuarios VALUES ({}, "{}", "{}", "{}", {});'.format(
            id, nombre, apellido, correo, dni))

data_personales(1000)
# GENERA GRACIAS AL PROVIDE DE internet, una imagen cuyo ancho y alto sera de 100px
# print(fake.image_url(width=100, height=100))
# GENERAR 500 empleados
# print(fake.unique.first_name())
# GENERA UN APELLIDO ALEATORIO
# print(fake.last_name())
# GENERA UN CORREO ALEATORIO
# print(fake.email())
# GENERA UN NOMBRE ALEATORIO
# print(fake.first_name())
# GENERA UN NUMERO RANDOM ALEATORIO
# print(fake.random_int(min=1, max=501))