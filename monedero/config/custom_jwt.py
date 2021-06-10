# funcion para personalizar el error de mi libreria de JWT
def manejo_error_JWT(error):
    print(error)
    print(type(error))
    print(error.status_code)
    print(error.description)
    print(error.headers)
    print(error.error)
    respuesta = {
        "success": False,
        "content": None,
        "message": None
    }
    if error.error == 'Authorization Required':
        respuesta["message"]="Se necesita una token para esta peticion"
    elif error.error == 'Bad Request':
        respuesta["message"]="Credenciales invalidas"
    elif error.error == 'Signature has expired':
        respuesta["message"]="El token ya expiro"
    elif error.error == 'Signature verification failed':
        respuesta["message"]="Token invalido"
    elif error.error == 'Unsupported authorization type':
        respuesta["message"]="Tipo no autorizado"
    else:
        respuesta["message"]="Error desconocido"
    return respuesta, error.status_code

    # 401 => unauthorized => no autorizado