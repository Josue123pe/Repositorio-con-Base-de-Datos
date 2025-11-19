from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import proveedor_schema
from services import proveedor_service
from database.database import get_db

router = APIRouter()

@router.post("/proveedores/", response_model=proveedor_schema.Proveedor, tags=["Proveedores"])
def create_proveedor(proveedor: proveedor_schema.ProveedorCreate, db: Session = Depends(get_db)):
    return proveedor_service.create_proveedor(db=db, proveedor=proveedor)

@router.get("/proveedores/", response_model=List[proveedor_schema.Proveedor], tags=["Proveedores"])
def read_proveedores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    proveedores = proveedor_service.get_proveedores(db, skip=skip, limit=limit)
    return proveedores

@router.get("/proveedores/{proveedor_id}", response_model=proveedor_schema.Proveedor, tags=["Proveedores"])
def read_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    db_proveedor = proveedor_service.get_proveedor(db, proveedor_id=proveedor_id)
    if db_proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor not found")
    return db_proveedor

@router.put("/proveedores/{proveedor_id}", response_model=proveedor_schema.Proveedor, tags=["Proveedores"])
def update_proveedor(proveedor_id: int, proveedor: proveedor_schema.ProveedorUpdate, db: Session = Depends(get_db)):
    db_proveedor = proveedor_service.update_proveedor(db, proveedor_id=proveedor_id, proveedor=proveedor)
    if db_proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor not found")
    return db_proveedor

@router.delete("/proveedores/{proveedor_id}", response_model=proveedor_schema.Proveedor, tags=["Proveedores"])
def delete_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    db_proveedor = proveedor_service.delete_proveedor(db, proveedor_id=proveedor_id)
    if db_proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor not found")
    return db_proveedor
