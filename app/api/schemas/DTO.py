from pydantic import BaseModel, Field
from datetime import date 

class UsuarioDTOPeticion(BaseModel):
    nombre: str 
    edad: int
    telefono: str
    correo: str
    contraseña: str
    fechaRegistro: date
    ciudad: str
    class Config:
        orn_mode=True

class UsuarioDTORespuesta():
    id: int
    nombre: str
    telefono: str
    ciudad: str
    
    class Config:
        orn_mode=True


class GastoDTOPeticion(BaseModel):
    monto: str
    fecha: date
    
    nombre: str
    descripcion: str
    class Config:
        orn_mode=True

class GastoDTORespuesta():
    id: int
    monto: str
    fecha: date
    nombre: str
    descripcion: str 
    class Config:
        orn_mode=True


class CategoriaDTOPeticion(BaseModel):
     
    nombreCategoria:str
    descripcion:str
    fotoIcono:str
    class Config:
        orn_mode=True

class CategoriaDTORespuesta():
    id: int
    nombre: str
    nombreCategoria: str
    descripcion: str


    class Config:
        orn_mode=True


class MetodoPagoDTOPeticion(BaseModel):
    nombreMetodo: str
    descripcion: str
    fotoIcono: str
    entidad: str
    class Config:
        orn_mode=True

class MetodoPagoDTORespuesta():
    id: int
    nombreMetodo: str
    descripcion: str
    entidad:str 

    class Config:
        orn_mode=True


class FacturaDTOPeticion(BaseModel):
    fecha: date
    monto: int
    descripcion:str
    class Config:
        orn_mode=True

class FacturaDTORespuesta():
    id: int
    fecha: date
    monto: int
    descripcion:str
    class Config:
        orn_mode=True
