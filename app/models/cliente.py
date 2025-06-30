from sqlalchemy import Column, Integer, String
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nit = Column(String, nullable=False)
    razon_social = Column(String, nullable=False)
    correo = Column(String)
    telefono = Column(String)
    direccion = Column(String)