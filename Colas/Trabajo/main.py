
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from paquete.cola import Cola

app = FastAPI()
cola = Cola()

class Item(BaseModel):
    nombre: str
    productos: List[str]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/estado")
def estado():
    elementos = cola.contar()
    return {"status": "ok", "elementos": elementos}

@app.post("/encolar", status_code=200)
def encolar(item: Item):
    cola.encolar(item.dict())  
    return {"status": "ok", "message_id": item.nombre} 

@app.get("/desencolar")
def desencolar():
    elemento = cola.desencolar()
    if elemento:
        return {"status": "ok", "elemento": elemento}
    else:
        raise HTTPException(status_code=404, detail="No hay elementos en la cola")

@app.get("/ver_todos")
def ver_todos():
    elementos = cola.ver_listado()
    return {"status": "ok", "elementos": elementos}

@app.get("/ver_primero")
def ver_primero():
    elemento = cola.ver_primero()
    if elemento:
        return {"status": "ok", "elemento": elemento}
    else:
        raise HTTPException(status_code=404, detail="No hay elementos en la cola")

@app.get("/ver_ultimo")
def ver_ultimo():
    elemento = cola.ver_ultimo()
    if elemento:
        return {"status": "ok", "elemento": elemento}
    else:
        raise HTTPException(status_code=404, detail="No hay elementos en la cola")

@app.get("/cancelar_pedido/{mensaje_id}")
def cancelar_pedido(mensaje_id: int):
    elemento = cola.desencolar_id(mensaje_id)
    if elemento:
        return {"status": "ok", "message_id": mensaje_id, "message": "Pedido cancelado"}
    else:
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
