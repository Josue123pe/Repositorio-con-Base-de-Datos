from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import categoria_schema
from services import categoria_service
from database.database import get_db

router = APIRouter()

@router.post("/categorias/", response_model=categoria_schema.Categoria, tags=["Categorias"])
def create_categoria(categoria: categoria_schema.CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_service.create_categoria(db=db, categoria=categoria)

@router.get("/categorias/", response_model=List[categoria_schema.Categoria], tags=["Categorias"])
def read_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorias = categoria_service.get_categorias(db, skip=skip, limit=limit)
    return categorias

@router.get("/categorias/{categoria_id}", response_model=categoria_schema.Categoria, tags=["Categorias"])
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = categoria_service.get_categoria(db, categoria_id=categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return db_categoria

@router.put("/categorias/{categoria_id}", response_model=categoria_schema.Categoria, tags=["Categorias"])
def update_categoria(categoria_id: int, categoria: categoria_schema.CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = categoria_service.update_categoria(db, categoria_id=categoria_id, categoria=categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return db_categoria

@router.delete("/categorias/{categoria_id}", response_model=categoria_schema.Categoria, tags=["Categorias"])
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = categoria_service.delete_categoria(db, categoria_id=categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return db_categoria
