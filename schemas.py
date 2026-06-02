from pydantic import BaseModel

# --- Esquemas de Producto ---
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    categoria_id: int

class ProductoResponse(ProductoCreate):
    id: int
    
    class Config:
        orm_mode = True

# --- Esquemas de Categoría ---
class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int
    
    class Config:
        orm_mode = True