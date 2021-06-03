from config.conexion_bd import base_de_datos
from sqlalchemy import Column, types, orm

class PostreModel(base_de_datos.Model):
    # para cambiar el nombre de la tabla en la bd
    __tablename__ = "postres"
    postreId = Column(name='id', primary_key=True, 
                        autoincrement=True,unique=True, type_=types.Integer)
    postreNombre = Column(name='nombre', type_=types.String(length=45))
    postrePorcion = Column(name='porcion',type_=types.String(length=25))

    #El relationshipo sirve para indicar todos lo s"hijos"" que puede tener ese modelo 9todas sus FK)
    #que puedan existir en determinado modelo
    #el backref creara un atributo virtual en el model del hijo (Preparacion) para que pueda acceder
    # a todo el objeto de PostreModel sin la necesidad de hacer una subconsulta (creara un join cuando 
    # sea necesario)
    # lazy => define cuando SQLAlchemy va a cargar la data adyacente de la base de datos
    # True/ 'select' => cargara todos los datos adyacentes
    # False/'join'   => solamente cargara cuando sea necesario (cuando se utilicen dichos datos)
    # 'subquery'     => trabajara los datos PERO en una subconsulta
    # 'dynamic'      => en este se pueden agregar filtros adicionales. SQLAlchemy devolvera otro objeto
    #                   dentro de la clase

    preparaciones = orm.relationship(
                    'PreparacionModel', backref='preparacionPostre', lazy=True)
    recetas = orm.relationship('RecetaModel',backref='recetaPostre')

    
    def __init__(self,nombre,porcion):
        self.postreNombre = nombre
        self.postrePorcion = porcion


    def __str__(self):
        return "El postre es {}".format(self.postreNombre)

    def save(self):
        #el metodo session.add crea una nueva sesion en la bd y ademas evita que se creen nuevas 
        #sesiones y asi relentizar la conexion a la bd
        #el metodo add sirve para agregar toda l ainstancia actual (mi nuevo postre) y corroborar con
        #las columnas de la bd si todo esta correcto
        #esto, ademas crea una transaccion en la cual sirve para agrupar varias sentencias de insert,
        #update, delete
        base_de_datos.session.add(self)
        #ahora si tdos los pasos de escritura, actualizacion y eliminacion de la bd fueron exitosos
        #entonces se guardaran todos los cambios de manera permanente
        base_de_datos.session.commit()
        #metodo que sirve para cerrar la sesion de la bd
        
        #al cerrar la base de datos, no se puede volver a escribir una peticion
        #base_de_datos.session.close()
    
    def json(self):
        return{
            "postreid": self.postreId,
            "postreNombre": self.postreNombre,
            "postrePorcion": self.postrePorcion
        }
