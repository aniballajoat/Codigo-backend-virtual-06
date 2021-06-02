# un controlador es el comportamiento que va a tener mi API cuando se llame a determinada ruta
# /postres GET => mostrar los postres
from flask_restful import Resource, reqparse
from models.postre import PostreModel

# serializer (serializador)
serializerPostres = reqparse.RequestParser(bundle_errors=True)
serializerPostres.add_argument(
    'nombre',               #nombre del atributo en el body
    type=str,               #tipo de dato que me tiene que mandar
    required=True,          #si es de caracter obligatorio o no
    help="falta el nombre", #mensaje de ayuda en el caso fuese obligatorio y no me lo mandase
    location='json'         #en que parte del request me mandara, ya sea json (body) o url
)

serializerPostres.add_argument(
    'porcion',
    type=str,
    required=True,
    help="Falta la porcion {error_msg}",
    choices=('Familiar','Personal','Mediano'),
    location='json'
)
class PostresController(Resource):
    def get(self):
        # SELECT * FROM postres;
        print(PostreModel.query.all())
        return 'ok'
    def post(self):
        data = serializerPostres.parse_args()
        print(data)
        return 'ok'
