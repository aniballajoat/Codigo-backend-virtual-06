# ejemplo:
# Para evitar que en cada impresion se ejecute en una nueva linea, se puede agregar el parametro end y este indicara como queremos que actue al finalizar la linea, su valor por defecto es \n, pero si le cambiamos a * entonces, al finalizar la impresion, colocara un asterisco en vez de un salto de linea
for numero in range(5):
    print(numero, end="*")

# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****

def rectangulo():
    a = int(input("ingrese primer valor: "))
    b = int(input("ingrese segundo valor: "))

    for i in range(a):
        for j in range (b):
            print('*',end="")
        print('\n')

# Escribir una funcion que nosotros le ingresemos el lado de un octagono y que lo dibuje
# Ejemplo:
# Lados: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****

def lados():
    a = int(input("Ingrese cantidad de lados: "))
    b = a - 1
    c = a
    for j in range(b):
        for k in range (b-j):
            print(" ",end="")
        for i in range (c):
            print("*",end="")
        c+=2
        print('\n')
    for i in range(a):
        for i in range(c):
            print("*",end="")
        print('\n')
    for j in range(a):
        for k in range (j):
            print(" ",end="")
        for i in range (c):
            print("*",end="")
        c-=2
        print('\n')
# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *
def triangulo():
    a = int(input("Ingrese Altura: "))
    while a > 0:
        for i in range (a):
            print("*",end="")
        print("\n")
        a-=1
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12
def collatz():
    a = int(input("ingrese un numero:"))
    print(a)
    while a!=1:
        a = int(a/2) if a%2==0 else  int(a*3 + 1)

        print(a)
# Una vez resuelto todos los ejercicios, crear un menu de seleccion que permita escoger
# que ejercicio queremos ejecutar hasta que escribamos "salir" ahi recien va a terminar
# de escoger el ejercicio
def operaciones():
    funcion = ""
    print("Bienvenido!")
    
    while 1==1:
        print("Ingrese que ejercicio desea revisar: ")
        print("- rectangulo")
        print("- lados")
        print("- triangulo")
        print("- collatz")
        print("Para salir, escriba 'salir'")

        funcion = input()
        if funcion == "rectangulo":
            rectangulo()
        elif funcion == "lados":
            lados()
        elif funcion == "triangulo":
            triangulo()
        elif funcion == "collatz":
            collatz()
        elif funcion == "salir":
            break
        else:
            print("ejercicio no reconocido, por favor ingrese operacion nuevamente")
operaciones()