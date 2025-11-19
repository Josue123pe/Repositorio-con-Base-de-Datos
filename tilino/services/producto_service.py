from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repositories import producto_repository, categoria_repository, proveedor_repository
from schemas import producto_schema

def get_producto(db: Session, producto_id: int):
    return producto_repository.get_producto(db=db, producto_id=producto_id)

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return producto_repository.get_productos(db=db, skip=skip, limit=limit)

def create_producto(db: Session, producto: producto_schema.ProductoCreate):
    # Validate Categoria
    if producto.categoria_id:
        db_categoria = categoria_repository.get_categoria(db, producto.categoria_id)
        if not db_categoria:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoría con id {producto.categoria_id} no encontrada.")

    # Validate Proveedor
    if producto.proveedor_id:
        db_proveedor = proveedor_repository.get_proveedor(db, producto.proveedor_id)
        if not db_proveedor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Proveedor con id {producto.proveedor_id} no encontrado.")

    return producto_repository.create_producto(db=db, producto=producto)

def update_producto(db: Session, producto_id: int, producto: producto_schema.ProductoUpdate):
    # Validate Categoria
    if producto.categoria_id:
        db_categoria = categoria_repository.get_categoria(db, producto.categoria_id)
        if not db_categoria:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoría con id {producto.categoria_id} no encontrada.")

    # Validate Proveedor
    if producto.proveedor_id:
        db_proveedor = proveedor_repository.get_proveedor(db, producto.proveedor_id)
        if not db_proveedor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Proveedor con id {producto.proveedor_id} no encontrado.")

    db_producto = producto_repository.get_producto(db, producto_id=producto_id)
    if not db_producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Producto con id {producto_id} no encontrado.")

    return producto_repository.update_producto(db=db, producto_id=producto_id, producto=producto)

def delete_producto(db: Session, producto_id: int):
    db_producto = producto_repository.get_producto(db, producto_id=producto_id)
    if not db_producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Producto con id {producto_id} no encontrado.")
        
    return producto_repository.delete_producto(db=db, producto_id=producto_id)
