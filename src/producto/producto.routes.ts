import { Router } from "express";
import { actualizarProductoDto } from "./dto.request";
import { 
    actualizarProducto, 
    crearProducto, 
    eliminarProducto, 
    mostrarProductos,
 } from "./producto.controllers";

export const productoRouter = Router();

productoRouter
        .route("/productos")
        .post(crearProducto)
        .get(mostrarProductos);

productoRouter
        .route("/productos/:id")
        .put(actualizarProducto)
        .put(actualizarProductoDto,actualizarProducto)
        .delete(eliminarProducto);