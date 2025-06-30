from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.cliente import ClienteCreate, ClienteOut
from app.crud import cliente as crud_cliente

router = APIRouter(prefix="/clientes", tags=["clientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClienteOut)
def crear(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return crud_cliente.crear_cliente(db, cliente)

@router.get("/", response_model=list[ClienteOut])
def listar(db: Session = Depends(get_db)):
    return crud_cliente.obtener_clientes(db)

@router.get("/buscar", response_model=list[ClienteOut])
def buscar(q: str, db: Session = Depends(get_db)):
    return crud_cliente.buscar_clientes(db, q)
