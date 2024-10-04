from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion,UsuarioDTORespuesta,GastoDTOPeticion,GastoDTORespuesta,CategoriaDTOPeticion,CategoriaDTORespuesta,MetodoPagoDTOPeticion,MetodoPagoDTORespuesta,FacturaDTOPeticion,FacturaDTORespuesta
from app.api.models.modelosApp import Usuario, Gastos,Categoria,MetodoPago,Factura
from app.database.configuration import sessionLocal, engine

#para que una api funcione debe tener un archivo enrutador 

rutas= APIRouter()#ENDPOINTS

#crear una funcion para establecer cuando yo qyuera y necesite 
#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
     yield basedatos
    except Exception as error:
       basedatos.rollback()
       raise error
    finally:
       basedatos.close()
 #PROGRAMACION DE CADA UNO DE LOS SERVICIOS QUE OFRECERA NUESTRA API(BAsada en CRUD)
 #(DTO son datos que van y vienen y se ejecutan guardados en la base de datos)

 #SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN LA BASE DE DATOS
@rutas.post("/usuarios",response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion:UsuarioDTOPeticion,db:Session=Depends(getDataBase)):
   try:
      usuario= Usuario(
         nombre=datosPeticion.nombre,
         edad=datosPeticion.edad,
         telefono=datosPeticion.telefono,
         correo=datosPeticion.correo,
         contrasena=datosPeticion.correo,
         fechaRegistro=datosPeticion.fechaRegistro,
         ciudad=datosPeticion.ciudad
                       )
      
      db.add(usuario)
      db.commit()
      db.refresh()
      return usuario
   except Exception as error:
      db.rollback()
      raise HTTPException(status_code=400, detail="Error al regisytrar el usuario")
   


@rutas.post("/gastos",response_model=GastoDTOPeticion)
def guardarGasto(datosPeticion:GastoDTOPeticion,db:Session=Depends(getDataBase)):
   try:
      gastos=Gastos(
         monto=datosPeticion.monto,
         fecha=datosPeticion.fecha,
         descripcion=datosPeticion.descripcion,
         nombre=datosPeticion.nombre
        
       )
      
      db.add(gastos)
      db.commit()
      db.refresh()
      return gastos
   except Exception as errores:
      db.rollback()
      raise HTTPException()
   
@rutas.post("/categoria",response_model=CategoriaDTORespuesta)
def guardarCategoria(datosPeticion:CategoriaDTOPeticion,db:Session=Depends(getDataBase)):
   try:
      categoria=Categoria(
         nombreCategoria=datosPeticion.nombreCategoria,
         descripcion=datosPeticion.descripcion,
         fotoIcono=datosPeticion.fotoIcono

      )
      db.add(categoria)
      db.commit()
      db.refresh()
      return categoria
   except Exception as errores:
      db.rollback()
      raise HTTPException()
   
@rutas.post("/metodoPago",response_model=MetodoPagoDTORespuesta)
def guardarMetodoPago(datosPeticion:MetodoPagoDTOPeticion,db:Session=Depends(getDataBase)):
   try:
      metodoPago=MetodoPago(
       nombreMetodo=datosPeticion.nombreMetodo,
       descripcion=datosPeticion.descripcion,
       fotoIcono=datosPeticion.fotoIcono,
       entidad=datosPeticion.entidad

      )
      db.add(metodoPago)
      db.commit()
      db.refresh()
      return metodoPago
   except Exception as errores:
      db.rollback()
      raise HTTPException()
   


@rutas.get("/usuarios",response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
   try:
      listadoDeUsuarios=db.query(Usuario).all
      return listadoDeUsuarios
   except Exception as error:
      db.rollback()
      raise HTTPException()   


@rutas.post("/factura", response_model=FacturaDTORespuesta)
def guardarFactura(datosPeticion: FacturaDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        factura = Factura(
            fecha=datosPeticion.fecha,
            monto=datosPeticion.monto,
            descripcion=datosPeticion.descripcion
        )

        db.add(factura)
        db.commit()
        db.refresh(factura)  # Debes pasar el objeto factura aquí
        return factura
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al registrar la factura")




@rutas.get("/gatos",response_model=List[GastoDTORespuesta])
def buscarGastos(db:Session=Depends(getDataBase)):
   try:
      listadoDeGastos=db.query(Gastos).all
      return listadoDeGastos
   except Exception as error:
      db.rollback()
      raise HTTPException()   
   

   
@rutas.get("/categoria",response_model=List[CategoriaDTORespuesta])
def buscarCategoria(db:Session=Depends(getDataBase)):
   try:
      listadoDeCategoria=db.query(Categoria).all
      return listadoDeCategoria
   except Exception as error:
      db.rollback()
      raise HTTPException()   



@rutas.get("/metodoPago",response_model=List[MetodoPagoDTORespuesta])
def buscarMetodoPago(db:Session=Depends(getDataBase)):
   try:
      listadoDeMetodoPago=db.query(MetodoPago).all
      return listadoDeMetodoPago
   except Exception as error:
      db.rollback()
      raise HTTPException()   
