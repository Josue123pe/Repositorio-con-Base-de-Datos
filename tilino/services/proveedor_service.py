from sqlalchemy.orm import Session
from repositories import proveedor_repository
from schemas import proveedor_schema

def get_proveedor(db: Session, proveedor_id: int):
    return proveedor_repository.get_proveedor(db=db, proveedor_id=proveedor_id)

def get_proveedores(db: Session, skip: int = 0, limit: int = 100):
    return proveedor_repository.get_proveedores(db=db, skip=skip, limit=limit)

def create_proveedor(db: Session, proveedor: proveedor_schema.ProveedorCreate):
    return proveedor_repository.create_proveedor(db=db, proveedor=proveedor)

def update_proveedor(db: Session, proveedor_id: int, proveedor: proveedor_schema.ProveedorUpdate):
    return proveedor_repository.update_proveedor(db=db, proveedor_id=proveedor_id, proveedor=proveedor)

def delete_proveedor(db: Session, proveedor_id: int):
    return proveedor_repository.delete_proveedor(db=db, proveedor_id=proveedor_id)
