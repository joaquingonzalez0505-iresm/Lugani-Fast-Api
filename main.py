from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from database import get_db

app = FastAPI()

# --- Endpoints de Productos ---

@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtainer_productos(db)

@app.post("/productos", response_model=schemas.ProductoCreate)
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.put("/productos/{id}", response_model=schemas.ProductoCreate)
def actualizar_producto(id: int, datos: schemas.ProductoCreate, db: Session = Depends(get_db)):
    producto = crud.actualizar_producto(db, producto_id=id, datos=datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.delete("/productos/{id}")
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, producto_id=id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado"}

