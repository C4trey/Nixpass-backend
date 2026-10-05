from fastapi import FastAPI
from . import models
from .database import engine

# Crea las tablas en PostgreSQL si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NixPass API")

@app.get("/")
def read_root():
    return {"status": "Backend Zero-Knowledge activo y conectado a PostgreSQL"}