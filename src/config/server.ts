import express, { Request, Response, Express, NextFunction } from "express";
import morgan from "morgan";
import { json } from "body-parser";
import { tipoRouter } from "../routes/tipo";
import { accionRouter } from "../routes/accion";
import { usuarioRouter } from "../routes/usuario";
import conexion from "./sequelize";
import { productoRouter } from "../routes/producto";
import { imagenRouter } from "../routes/imagen";
import { movimientoRouter } from "../routes/movimiento";
import documentation from "./swagger.json"
import swaggerUI from "swagger-ui-express"

require("dotenv").config();
export default class Server {
  app: Express;
  port: string = "";

  constructor() {
    this.app = express();
    this.port = process.env.PORT || "8000";
    this.bodyParser();
    this.CORS();
    this.rutas();
  }

  bodyParser() {
    this.app.use(json());
    this.app.use(morgan("dev"));
  }

  CORS(){
    this.app.use((req: Request, res: Response, next: NextFunction)=>{
      // Access-Control-Allow-Origin => indicar que origenes (dominios pueden acceder a mi API)
      res.header('Access-Control-Allow-Origin','*')
      // Access-Control-Allow-Headers => indicar que tipos de cabeceras pueden ser enviadas
      res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
      // Access-Control-Allow-Methods => indica que metodos pueden ser intentar acceder a mi backend
      res.header('Access-control-Allow-Methods', 'GET, POST, PUT, DELETE')
      // si es que cumple el origen (dominio), el header y el metodo entonces daremos paso al controlador solicitado
      next();
    });
  }

  rutas() {
    this.app.get("/", (req: Request, res: Response) => {
      res.send("Bienvenido a la api de zapateria");
    });
    this.app.use("/docs", swaggerUI.serve, swaggerUI.setup(documentation));
    this.app.use(tipoRouter);
    this.app.use(accionRouter);
    this.app.use(usuarioRouter);
    this.app.use(productoRouter);
    this.app.use(imagenRouter);
    this.app.use(movimientoRouter);
  }

  start() {
    this.app.listen(this.port, async () => {
      console.log("Servidor corriendo exitosamente");
      try {
        // el alter a diferencia del force lo que realizara sera que si una columna o varias es modificada y si es que tiene informacion es aceptable en la nueva variacion o si es que no tuviese informacion para casos de eliminacion de columnas
        // { alter: true }
        await conexion.sync();
        console.log("Base de datos sincronizada exitosamente");
      } catch (e) {
        console.error(e);
      }
    });
  }
}