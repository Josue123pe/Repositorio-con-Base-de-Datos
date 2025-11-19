from fastapi import FastAPI
from database import models
from database.database import engine
from apis import producto_api, categoria_api, proveedor_api

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tilin API",
    description="API para gestionar productos, categorías y proveedores.",
    version="1.0.0",
)

app.include_router(producto_api.router)
app.include_router(categoria_api.router)
app.include_router(proveedor_api.router)

@app.get("/")
def read_root():
    return {"Project": "Tilin API"}
