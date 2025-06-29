from pydantic import BaseModel

# Base (campos comunes para crear y actualizar)
class ClienteBase(BaseModel):
    nit: str
    razon_social: str
    correo: str | None = None
    telefono: str | None = None
    direccion: str | None = None

# Esquema para crear
class ClienteCreate(ClienteBase):
    pass

# Esquema para respuesta con ID incluido
class ClienteOut(ClienteBase):
    id: int

    class Config:
        from_attributes = True
