from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from utils import verify_password
from auth import crear_token
from deps import get_current_user, require_admin    
from pydantic import BaseModel   # IMPORTANTE: Cambialo por el nombre que le hayas puesto a tu archivo de modelos/tablas (ej: models.py)

app = FastAPI()

# Definición del modelo de datos para validación
class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool

# Base de datos en memoria (Lista de objetos Producto)
productos = []

# 1. LISTAR PRODUCTOS (GET)
@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)
# 2. AGREGAR PRODUCTO CON MODELO (POST)
@app.post("/productos", response_model=schemas.ProductoResponse)
def agregar_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

# 3. ACTUALIZAR PRODUCTO (PUT)
# Nota: El documento mantiene la actualización simple por nombre en esta sección
@app.put("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def actualizar_producto(producto_id: int, datos: schemas.ProductoCreate, db: Session = Depends(get_db)):
    producto = crud.actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# 4. ELIMINAR PRODUCTO (DELETE)
@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado"}

### Categoria ##

@app.post("/categorias", response_model=schemas.CategoriaResponse)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@app.get("/categorias", response_model=list[schemas.CategoriaResponse])
def listar_categoria(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db)

#Usuarios

@app.post("/usuarios", response_model=schemas.UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.crear_usuario(db, usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.obtener_usuario_por_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    token = crear_token(sub=user.email, es_admin=user.es_admin)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/usuarios/me", response_model=schemas.UsuarioResponse)
def leer_perfil(current_user = Depends(get_current_user)):
    return current_user


@app.get("/admin/ping")
def admin_ping(_admin = Depends(require_admin)):
    return {"ok": True, "role": "admin"}