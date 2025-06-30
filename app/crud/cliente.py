from sqlalchemy.orm import Session
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate

def crear_cliente(db: Session, cliente: ClienteCreate):
    nuevo = Cliente(**cliente.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_clientes(db: Session):
    return db.query(Cliente).all()

def buscar_clientes(db: Session, query: str):
    return db.query(Cliente).filter(Cliente.razon_social.ilike(f"%{query}%")).all()
