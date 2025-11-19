from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), unique=True, index=True)

    productos = relationship("Producto", back_populates="categoria")

class Proveedor(Base):
    __tablename__ = "proveedor"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), index=True)
    telefono = Column(String(20), nullable=True)

    productos = relationship("Producto", back_populates="proveedor")


class Producto(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), index=True)
    cantidad = Column(Integer)
    categoria_id = Column(Integer, ForeignKey("categoria.id"))
    proveedor_id = Column(Integer, ForeignKey("proveedor.id"))

    categoria = relationship("Categoria", back_populates="productos")
    proveedor = relationship("Proveedor", back_populates="productos")
