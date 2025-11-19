from sqlalchemy.orm import Session
from repositories import categoria_repository
from schemas import categoria_schema

def get_categoria(db: Session, categoria_id: int):
    return categoria_repository.get_categoria(db=db, categoria_id=categoria_id)

def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return categoria_repository.get_categorias(db=db, skip=skip, limit=limit)

def create_categoria(db: Session, categoria: categoria_schema.CategoriaCreate):
    return categoria_repository.create_categoria(db=db, categoria=categoria)

def update_categoria(db: Session, categoria_id: int, categoria: categoria_schema.CategoriaCreate):
    return categoria_repository.update_categoria(db=db, categoria_id=categoria_id, categoria=categoria)

def delete_categoria(db: Session, categoria_id: int):
    return categoria_repository.delete_categoria(db=db, categoria_id=categoria_id)
