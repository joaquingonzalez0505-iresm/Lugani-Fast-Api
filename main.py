from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}


@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)


@app.post("/productos", response_model=schemas.ProductoResponse)
def agregar_producto(
    producto: schemas.ProductoCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_producto(db, producto)


@app.put("/productos/{producto_id}")
def actualizar_producto(
    producto_id: int,
    datos: schemas.ProductoCreate,
    db: Session = Depends(get_db)
):
    producto = crud.actualizar_producto(db, producto_id, datos)

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto


@app.post("/categorias", response_model=schemas.CategoriaResponse)
def crear_categoria(
    categoria: schemas.CategoriaCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_categoria(db, categoria)


@app.get("/categorias", response_model=list[schemas.CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.obtener_categoria(db)