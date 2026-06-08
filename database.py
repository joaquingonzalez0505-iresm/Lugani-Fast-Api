from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

# URL de conexión a PostgreSQL (Usuario: postgres, Contraseña: 123, BD: ecommerce_db)
DATABASE_URL = "postgresql://postgres:49455950@localhost:5432/ecommerce_db"

# Creación del motor de la base de datos
engine = create_engine(DATABASE_URL)

# Configuración de la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para que hereden los modelos
Base = declarative_base()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally :
        db.close()
        