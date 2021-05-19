edad = input("Ingresa tu edad: ")
print(type(edad))

edadEntero = int(edad)
print(type(edadEntero))

restriccion_edad=18
if edadEntero >= restriccion_edad and edadEntero < 65:
    print("Eres mayor de edad, ya puedes viajar")
elif edadEntero>=65:
    print("Puedes irte a un crucero")
else:
    print("Eres menor de edad, aun no puedes hacer nada >.<")
print("yo soy el codigo comun y corriente")

respuesta = 'eres mayor de edad' if(edadEntero>=18) else "eres menor de edad"
print(respuesta)

#nuumero si es + o - o 0

numero = int(input("ingrese el numero: "))

if(numero > 0):
    res = "es positivo"
elif (numero < 0):
    res = "es negativo"
else:
    res = "numero es 0"
print (res)

#indicar cuales son + y cuales -

numeros = [1,-4,5,-14,-16,-50,6,-100]
contpos = 0
contmen = 0
cont0 = 0
for elem in numeros:
    if elem >0:
        contpos +=1
    elif elem <0:
        contmen +=1
    else:
        cont0 +=1

print("hay ",contpos,"positivos, ",contmen," negativos y ", cont0, " ceros.")

numeros = [1,2,5,9,12,15,10,34,867,67]

#indicar si son multiplos de 3 y 5, ademas si hay multiplo de ambos no contarlo
cuenta5 = 0
cuenta3 = 0
for numero in numeros:
    if numero%3==0:
        if numero%5==0:
            continue
        else:
            cuenta3+=1
    elif numero%5==0:
        cuenta5+=1
print ("multiplos de 5: ",cuenta5, " y multiplos de 3: ",cuenta3)

inscritos = ["raul","pedro","maria","roxana", "margioret"]

nombres = []
print("ingrese 3 nombres")
for ingresa in range (3):
    name=input()
    nombres.append(name)
for names in nombres:
    if names in inscritos:
        print("el nombre: '",names, "' si esta")