from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
import crud
# pyrefly: ignore [missing-import]
from app.deps.deps import get_db, require_admin

router = APIRouter()

@router.get("/", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)

@router.post("/", response_model=schemas.ProductoResponse, dependencies=[Depends(require_admin)])
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@router.put("/{producto_id}", response_model=schemas.ProductoResponse)
def actualizar_producto(producto_id: int, datos: schemas.ProductoCreate, db: Session = Depends(get_db)):
    producto = crud.actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.delete("/{producto_id}", dependencies=[Depends(require_admin)])
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado"}