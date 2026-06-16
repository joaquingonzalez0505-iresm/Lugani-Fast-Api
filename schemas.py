from pydantic import BaseModel, EmailStr

# --- Esquemas de Producto ---
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    categoria_id: int

class ProductoResponse(ProductoCreate):
    id: int

    class Config:
        from_attributes = True

# --- Esquemas de Categoría ---
class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int

    class Config:
        from_attributes = True




#Usuario

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr


class UsuarioCreate(UsuarioBase):
    password: str
    es_admin: bool = False


class UsuarioResponse(UsuarioBase):
    id: int
    es_admin: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"