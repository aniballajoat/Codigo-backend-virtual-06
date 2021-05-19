libro = {
    "nombre": "Harry Potter",
    "autor": "J.K. Rowling",
    "editorial": "Blablabla",
    "año": 2018,
    "idiomas": [
        {
            "nombre": "portuges"
        },
        {
            "nombre": "ingles",
            "nombre": "ingles britanico"
        },
        {
            "nombre": "frances"
        },
        {
            "nombre": "aleman"
        },
    ],
    "calificacion": 5,
    "imdb": "00asd12-asd878-a4s5d4a5-a45sd4a5sd",
    "tomos": ("La piedra filosofal", "La camara secreta", "El vuelo del fenix")
}

#1
print(f"El autor del libro es {libro['autor']}")
#2
print("el segundo tomo es ",libro['tomos'][1])
#3
print("la cantidad de idiomas es ",len(libro["idiomas"]))
#4
if {"nombre":"ruso"} in libro["idiomas"]:
    print("el idioma ruso esta")
else:    
    print("el idioma no ruso esta")