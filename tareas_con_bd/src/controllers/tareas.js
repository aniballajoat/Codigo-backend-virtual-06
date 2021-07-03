import { Tarea } from "../config/modelos";
export const serializadorTarea = (req,res,next)=>{
    // analizamos el body
    const {tareaNombre}=req.body;
    // si no hay nombre
    if(tareaNombre && tareaNombre.trim().length > 0){
        next();
    }else{
        return res
        .json({
            success:false,
            content:"Se necesita un nombre",
            message:"error al crear la nueva tarea"
        })
        .status(400);
    }
};
// CRUD
export const crearTarea = async (req,res)=>{
    // para registrar una nueva tarea
    // si usamos el buids() se tendra que realizar en 2 pasos el guardado del registro, primero construyo el objeto
    // luego llamaria al metodo save()
    // Tarea.build({tareaNombre:'Hacer el MER',...}).save

    // el segundo metodo (1 solo paso)
    //{
    //  nombre:"hacer el mer",
    //}
    try
    {
        const muevaTarea = await Tarea.create(req.body);
        const datos = {tareaId,tareaNombre};
        return res
        .json({
            success: true,
            content: datos,
            message:"Nueva tarea creada con exito",
        })
        .status(201);
    } catch(error){
        return res.json({
            success: false,
            content: null,
            message:"No se pudo crear la tarea",
        })
        .status(400);
    }
};

export const listarTareas = async(req,res)=>{
    // para seleccionar que atributos queremos mostrar usaremos la clausula attributes y tendremos
    // que indicar en forma de un array todos los elementos a mostrar(tienen que ser los que definimos en el model)
    // y si queremos modificar el nombre entonces usaremos un array para indicar en la primera posicion el nombre 
    // de la columna en la bd y luego el nombre a mostrar
    const tareas = await Tarea.findAll({
        // attributes:["tareaNombre",["id","id de la tarea"]],
        //attributes:[["nombre","nombre de la tarea"],["id","id"]],
        attributes:{
            exclude: ["createdAt"],
        },
    });
    return res.json({
        success: true,
        content: tareas,
        message: null,
    });
};