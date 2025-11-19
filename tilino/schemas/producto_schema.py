from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    cantidad: int
    categoria_id: Optional[int] = None
    proveedor_id: Optional[int] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    cantidad: Optional[int] = None
    categoria_id: Optional[int] = None
    proveedor_id: Optional[int] = None

class Producto(ProductoBase):
    id: int

    class Config:
        orm_mode = True
