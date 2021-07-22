import { compareSync } from "bcrypt";
import { sign } from "jsonwebtoken";
import { Request, Response } from "express";
import { Usuario } from "./usuario.model";

export const registro = async (req: Request, res: Response) => {
  // crear el dto y validar los campos necesarios
  try {
    const nuevoUsuario = await Usuario.create(req.body);

    const data = nuevoUsuario.toJSON();

    delete data["usuarioPassword"];

    return res.status(201).json({
      success: true,
      content: data,
      message: "Usuario creado exitosamente",
    });
  } catch (error) {
    return res.status(400).json({
      success: false,
      content: error,
      message: "error al guardar el usuario",
    });
  }
};

export const login = async (req: Request, res: Response) => {
  const { correo, password } = req.body;
  const usuario = await Usuario.findOne(
    { usuarioCorreo: correo },
    "usuarioPassword usuarioTipo"
  );
  // console.log(usuario);
  if (!usuario || usuario.usuarioTipo === "CLIENTE") {
    return res.status(404).json({
      success: false,
      message: "credenciales invalidas",
      content: null,
    });
  }

  const resultado = compareSync(password, usuario.usuarioPassword ?? "");

  if (resultado) {
    const payload = {
      usuarioId: usuario._id,
    };

    const token = sign(payload, process.env.JWT_SECRET ?? "", {
      expiresIn: "1h",
    });

    return res.status(200).json({
      success: true,
      content: token,
      message: null,
    });
  } else {
    return res.status(404).json({
      success: false,
      message: "credenciales invalidas",
      content: null,
    });
  }
};