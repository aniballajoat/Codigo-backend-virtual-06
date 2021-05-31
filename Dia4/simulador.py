from faker import Faker
from faker.providers import internet, misc

fake = Faker()
fake.add_provider(internet)
fake.add_provider(misc)



for id in range(1,501):
    nombre = fake.first_name()
    apellido = fake.last_name()
    identificador = fake.uuid4()
    departamento_id = fake.random_int(min=1,max=5)
    if id == 1:
        supervisor_id = "null"
    else:
        supervisor_id = fake.random_int(min=1,max=id)
    print("INSERT INTO PERSONALES VALUES({},'{}','{}','{}',{},{});".format(
        id, nombre,apellido,identificador,departamento_id,supervisor_id))


#Generar 500 empleados
"""
print(fake.image_url(width=100, height=100))
print(fake.unique.first_name())
print(fake.last_name())
print(fake.email())
print(fake.first_name())
print(fake.unique.random_int(min=1, max =501))
print(fake.uuid4())
#Generar data simulada de 500 personales
#Insert into personales values (1,"EDUARDO","DE RIVERO",uuid,2,null);
"""