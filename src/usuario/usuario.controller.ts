import { Request, Response } from "express";
import { Usuario } from "./usuario.model";
import { compareSync } from "bcrypt";
import { sign, TokenExpiredError } from "jsonwebtoken";



export const registro = async(req: Request, res:Response)=>{


    // crear el dto y validar los campos necesarios
    console.log(req.body);
    const nuevoUsuario = await Usuario.create(req.body);


    delete nuevoUsuario._doc["usuarioPassword"];
    return res.status(201).json({
        success: true,
        content: nuevoUsuario,
        message: "Usuario creado exitosamente",
    });

    // guarda el usuario en la bd y devolver todo el usuario menos la password
};

export const login = async(req: Request, res: Response)=>{
    const {correo, password}= req.body;
    const usuario = await Usuario.findOne (
        {usuarioCorreo: correo},
        "usuarioPassword usuarioTipo"
        );
    console.log(usuario);
    if (!usuario || usuario.usuarioTipo === "CLIENTE"){
        return res.status(404).json({
            success: false,
            message: "credenciales invalidas",
            content: null,
        });
    }
    const resultado = compareSync(password, usuario.usuarioPassword);


    if (resultado){
        const payload = {
            usuarioId: usuario._id,
        };
        sign(payload, process.env.JWT_SECRET ?? "", {
            expiresIn: "1h",
        });
        return res.status(200).json({
            success:true,
            content:TokenExpiredError,
            message:null,
        });
    }else {
        return res.status(404).json({
            success: false,
            message: "credenciales invalidas",
            content: null,
        });
    }
};