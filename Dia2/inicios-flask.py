from flask import Flask, request
from flask_cors import CORS

#print(__name__)
app = Flask(__name__)
CORS(app,methods=['GET',"POST"],origins=['*'])
productos = []

@app.route("/")
def inicio():
    print("Me hicieron un llamado")
    return "Salidos desde mi API",200

@app.route("/productos", methods = ['GET','POST'])
def gestion_productos():
    print(request.method)
    if request.method == "POST":
        data = request.get_json()
        print(data)
        productos.append(data)
        return{
            "message": "Producto creado exitosamente",
            "content": data
        }, 201
    elif request.method == "GET":
        return{
            "message": "Estos son los productos registrados",
            "content": productos
        },200

@app.route("/productos/<int:id>",methods=['PUT','DELETE','GET'])
def gestion_producto(id):
    print(id)
    if len(productos)<=id:
        return{
            "message": "Producto no encontrado"
        }, 404
    if request.method == 'GET':
        """    
            try:
                return{
                    "content": productos[id]
                },200
            except:
                return{
                    "message": "Producto no encontrado"
                },404
        """
        return{
            "content": productos[id]
        },200
    

    elif request.method == "DELETE":
        productos.pop(id)
        return{
            "message": "Producto eliminado exitosamente"
        }
    elif request.method == "PUT":
        data = request.get_json()
        productos[id] = data
        return{
            "message": "Producto actualizado exitosamente",
            "content": productos[id]
        }
    return "ok"

@app.route("/productos/buscar")
def buscar_productos():
    print(request.args.get("nombre", "NO HAY"))
    return "ok"

app.run(debug=True)