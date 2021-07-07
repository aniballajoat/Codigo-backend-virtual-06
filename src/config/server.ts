import express, { Request, Response, Express } from "express";
import { json } from "body-parser";
import conexion from "./sequelize";
import { tipoRouter } from "../routes/tipo";
import { accionRouter } from "../routes/accion";
import morgan from "morgan";

export default class Server {
  app: Express;
  port: string = "";

  constructor() {
    this.app = express();
    this.port = process.env.PORT || "8000";
    this.bodyParser();
    this.rutas();
  }

  bodyParser() {
    this.app.use(json());
    this.app.use(morgan("dev"));
  }

  rutas() {
    this.app.get("/", (req: Request, res: Response) => {
      res.send("Bienvenido a la api de zapateria");
    });
    this.app.use(tipoRouter);
    this.app.use(accionRouter);
  }

  start() {
    this.app.listen(this.port, async () => {
      console.log("Servidor corriendo exitosamente");
      try {
        await conexion.sync();
        console.log("Base de datos sincronizada exitosamente");
      } catch (e) {
        console.error(e);
      }
    });
  }
}