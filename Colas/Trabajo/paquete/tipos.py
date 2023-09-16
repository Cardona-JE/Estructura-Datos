from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    nombre: str
    productos: List[str]
    

