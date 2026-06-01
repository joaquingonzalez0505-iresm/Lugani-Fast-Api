from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definición del modelo de datos para validación
class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool

# Base de datos en memoria (Lista de objetos Producto)
productos = []

# 1. LISTAR PRODUCTOS (GET)
@app.get("/productos")
def listar_productos():
    return {"productos": productos}

# 2. AGREGAR PRODUCTO CON MODELO (POST)
@app.post("/productos")
def agregar_producto(producto: Producto):
    productos.append(producto)
    return {"mensaje": "Producto agregado", "producto": producto}

# 3. ACTUALIZAR PRODUCTO (PUT)
# Nota: El documento mantiene la actualización simple por nombre en esta sección
@app.put("/productos/{id}")
def actualizar_producto(id: int, nombre: str):
    productos[id] = nombre
    return {"mensaje": "Producto actualizado", "producto": nombre}

# 4. ELIMINAR PRODUCTO (DELETE)
@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    eliminado = productos.pop(id)
    return {"mensaje": "Producto eliminado", "producto": eliminado}
