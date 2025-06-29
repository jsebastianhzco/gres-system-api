import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# URL de conexión (usa tus propios datos aquí)
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Motor de conexión
engine = create_engine(DATABASE_URL)

# Sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para declarar los modelos
Base = declarative_base()
