from sqlalchemy import Column, Integer, String
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nit = Column(String(30), nullable=False)
    razon_social = Column(String(150), nullable=False)
    correo = Column(String(100))
    telefono = Column(String(30))
    direccion = Column(String(100))

