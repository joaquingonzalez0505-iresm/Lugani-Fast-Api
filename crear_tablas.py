from database import engine, Base
from models import *

# Ejecuta la creación de todas las tablas que hereden de Base
Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente")