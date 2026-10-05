from sqlalchemy import Column, Integer, String, LargeBinary
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    
    # Parámetros públicos de autenticación
    salt = Column(String, nullable=False) # Salt público para Argon2
    auth_token_hash = Column(String, nullable=False) # Hash del token validado por passlib
    
    # Bóveda cifrada
    vault_nonce = Column(String, nullable=True) # El nonce que rota en cada modificación
    vault_blob = Column(LargeBinary, nullable=True) # El JSON encriptado con AES-GCM