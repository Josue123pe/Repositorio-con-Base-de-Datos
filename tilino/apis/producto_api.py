from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import producto_schema
from services import producto_service
from database.database import get_db

router = APIRouter()

@router.post("/productos/", response_model=producto_schema.Producto, tags=["Productos"])
def create_producto(producto: producto_schema.ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.create_producto(db=db, producto=producto)

@router.get("/productos/", response_model=List[producto_schema.Producto], tags=["Productos"])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    productos = producto_service.get_productos(db, skip=skip, limit=limit)
    return productos

@router.get("/productos/{producto_id}", response_model=producto_schema.Producto, tags=["Productos"])
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = producto_service.get_producto(db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

@router.put("/productos/{producto_id}", response_model=producto_schema.Producto, tags=["Productos"])
def update_producto(producto_id: int, producto: producto_schema.ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = producto_service.update_producto(db, producto_id=producto_id, producto=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

@router.delete("/productos/{producto_id}", response_model=producto_schema.Producto, tags=["Productos"])
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = producto_service.delete_producto(db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto
