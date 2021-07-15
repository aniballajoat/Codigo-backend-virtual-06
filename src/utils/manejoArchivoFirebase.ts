import { Storage } from "@google-cloud/storage";
import { Express } from "express";

require("dotenv").config()
// Creao la instancia de la clase Storage con la configuracion de las credenciales y el id del proyecto
const storage = new Storage({
  projectId: "zapateria-codigo-eduardo",
  credentials: {
    client_email: process.env.CLIENT_EMAIL_FIREBASE,
    //'firebase-adminsdk-dofzj@zapateria-codigo-anibal.iam.gserviceaccount.com',
    private_key: process.env.PRIVATE_KEY_FIREBASE?.replace(/\\n/gm,"n"),
    //'-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDBGYyM2BHH68T8\n5K6jXO4OvTXIXcoFdd5/ZYblBZ8Je+DuHejrZ7Ha1bNt2hBAZ/0Wo8O34UEBpDTM\nNRyjvSSdUPa7rVnC8oCiZ51X/fix8wYIcXDIRMmbHR4NxQnrqoZArIDr9suIS0ns\nSOeQBwGhgPQA05BRwNj8FbQzj67gALjih+8TmGvKSK5nOnegoQQLKVDLEzaKvJ7G\nuJ2RIs9C3nY5ISgy4RyUp2F2pIg4FqGaWsgAUmNjjDd0Y+2i1aWkHJGjKzbvsme7\nOhtXbptoEN7o7N1ExQ0B5j9Prye6o56itOl0ZOfqJPbZxt5IPqqEjRQz+g4u0ZEb\nAaZ7oxQRAgMBAAECggEACOltksn9jxce4yeINk6ph3lcyDOo6VXaaBGG117KK1lB\n5Sdw+p1RaGa8tlUOMzTBadgyxhOhqQpbq/GHEfj+nbqQ+pIqbnx76pLi4H7eiZLs\nXDslD/8ZuVyPiKXnem6HLeiwNgOwushzv9GRC1UBcqNVj4y0EEvYz9COHaOT1+9o\nAOqQADLgSbF4Ho0KTWwFlckuRS6CkuTcCkxp3C2oQgGg+kmmRDhZK/60Ik+F8QJ3\nsrpnn8Ek9MiPMmZVO3d/qRX7n9Yvzrkb/w/LN893G5gB6PgxudrhSfYGhO3ippnv\nIBw8uiX2jEfmRUvo1AygTvA71GIHrVet7RHuaafTwQKBgQDxrnWnBz14yM1T0blT\nHnqgNOcc8Cyilh+1m6RpWGp7G4FLCFkvFtqfmtjawaoDJMm1sz11bq1YtFi3N6zH\nmphWcZyQVV48sdSsyqaQk2xjibZWvUl7MfPxgzUJQPqBH7Mjq2ggclWRP9yS2S4o\nLRdTPSdYN2QRvZdwfACpuJKaoQKBgQDMikJ4Dv1O8EdJBRDW8LlX2FohHojyMAOC\nSYrKV2vU1+38l+8qr95g7m7ynrSQ28kGwkxybrVkEZ+79AIjREKsUwVV3NBG25jh\nG5yV1XtKQwrrHWuyDYSXrwldKhAFn666jAg7KdhZYnthirNs6GKMDmERLRXJCP8G\n5s+EfmbzcQKBgQCv2EP6V6Y+b7wVtI6nD5IhZtyRjZ6sXZaMyMYDcDVphUW5lkVt\noa9IWZ5W7HoK94VcEyIwg2rVE8NI69VnFfCpVNiZm8OJXcpkPr6aiuleMyDcU7VX\nUa0wmErKhOC/epUY6upEUWw41sJihmqzCLvj8Kbj5MmGru+1BERnOMhSgQKBgFg+\n8mx/8xPCoM7FK73AQAbBZilR1j2/L1RfzEx+KRy8SIYpOtuM4wGo/R8aD8dLu9B5\ntafNUd8pp2Pc46s5gRZ9/xhLW2Smy6+bTRRr9XRVtnk3yUYZhPI4Z27VffIfMbB0\nR/zWkewGjDrKL502KYZJkeFqNTL1+amNnUyJiHtRAoGAF23cyZAo839Ev5Sqot+f\ng0q7Mxw6c2M6WCcqBXnw2/8Sub3E7rFmijK8PqZQWqDE4hi3pup/efE2X5BLFHOV\nZsqAM42cuXmiYcLQ/oKhbjGE4ABJw7YBvvnZeydCi5PiGNxfxuu2qYCrADW8+4ga\nX3+MV83Fo6YXJMnkrN8V18g=\n-----END PRIVATE KEY-----\n'
  },
  //keyFilename: "./credenciales_firebase.json",
});
// Enlazo mi bucket (donde se almacenaran todas las imagenes)
// se copia el link que muestra el bucket PERO sin el protocolo gs ni el / del final
const bucket = storage.bucket("zapateria-codigo-eduardo.appspot.com");

export const subirArchivoUtil = (
  archivo: Express.Multer.File,
  path: string
): Promise<string> => {
  return new Promise((resolve, reject) => {
    if (!archivo) {
      reject("No se encontro el archivo");
    }
    // comienza el proceso de subida de imagenes

    const newFile = bucket.file(`${path}/${archivo.originalname}`);

    // agregar configuracion adicional de nuestro archivo como su metadata
    const blobStream = newFile.createWriteStream({
      metadata: {
        contentType: archivo.mimetype,
      },
    });

    // ahora puedo escuchar sus eventos (socket)
    blobStream.on("error", (error) => {
      reject(error.message);
    });

    // veremos el evento si es que la carga termino exitosamente
    blobStream.on("finish", async () => {
      try {
        const link = await newFile.getSignedUrl({
          action: "read",
          // La fecha actual + 1000 ms * segundos * minutos => cuantoas horas durara la token
          expires: Date.now() + 1000 * 60 * 60, // caducara en una hora
        }); // MM-DD-YYYY
        // return link;
        return resolve(link.toString());
      } catch (error) {
        reject(error);
      }
    });

    // aca se le indica que el procedimiento terminara pero que para que gestione todo la transferencia del archivo se el enviara sus bytes
    blobStream.end(archivo.buffer);
  });
};

export const generarUrl = async (
  carpeta: string,
  fileName: string
): Promise<string> => {
  try {
    const url = await bucket.file(`${carpeta}/${fileName}`).getSignedUrl({
      action: "read",
      expires: Date.now() + 1000 * 60 * 60,
    });
    return url.toString();
  } catch (error) {
    return error;
  }
};

export const eliminarArchivoUtitl = async (
  carpeta: string,
  archivo: string
) => {
  try {
    const respuesta = await bucket
      .file(`${carpeta}/${archivo}`)
      .delete({ ignoreNotFound: true });

    console.log(respuesta);

    return respuesta;
  } catch (error) {
    return error;
  }
};