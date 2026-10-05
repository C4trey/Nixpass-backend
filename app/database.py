import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Motor de conexión a PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Fábrica de sesiones para las consultas
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para definir las tablas
Base = declarative_base()

# Dependencia para inyectar la sesión en las rutas de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()