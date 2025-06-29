from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas

# Crear cliente
def crear_cliente(db: Session, cliente: schemas.ClienteCreate):
    nuevo_cliente = models.Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

# Listar todos los clientes
def listar_clientes(db: Session):
    return db.query(models.Cliente).all()

# Obtener cliente por ID
def obtener_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

# Actualizar cliente
def actualizar_cliente(db: Session, cliente_id: int, datos: schemas.ClienteCreate):
    cliente = obtener_cliente(db, cliente_id)
    if cliente:
        for key, value in datos.dict().items():
            setattr(cliente, key, value)
        db.commit()
        db.refresh(cliente)
    return cliente

# Eliminar cliente
def eliminar_cliente(db: Session, cliente_id: int):
    cliente = obtener_cliente(db, cliente_id)
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente