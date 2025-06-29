from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
import app.models as models
import app.schemas as schemas
import app.crud as crud
from fastapi.middleware.cors import CORSMiddleware


# Crear las tablas automáticamente si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",  # Puerto de Vite
    "http://127.0.0.1:5173",  # Otra forma común
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta de prueba
@app.get("/")
def root():
    return {"msg": "API funcionando 🔥"}

# Crear cliente
@app.post("/clientes", response_model=schemas.ClienteOut)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.crear_cliente(db, cliente)

# Listar clientes
@app.get("/clientes", response_model=list[schemas.ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return crud.listar_clientes(db)

# Obtener cliente por ID
@app.get("/clientes/{cliente_id}", response_model=schemas.ClienteOut)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.obtener_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# Actualizar cliente
@app.put("/clientes/{cliente_id}", response_model=schemas.ClienteOut)
def actualizar_cliente(cliente_id: int, datos: schemas.ClienteCreate, db: Session = Depends(get_db)):
    cliente = crud.actualizar_cliente(db, cliente_id, datos)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# Eliminar cliente
@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.eliminar_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"ok": True}
