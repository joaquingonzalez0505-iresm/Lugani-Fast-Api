from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
import crud
# pyrefly: ignore [missing-import]
from app.deps.deps import get_db

router = APIRouter()

@router.post("/", response_model=schemas.CategoriaResponse)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@router.get("/", response_model=list[schemas.CategoriaResponse])
def listar_categoria(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db)