from pydantic import BaseModel
from datetime import datetime

from enum import Enum

class Category(Enum):
    SHOES = "shoes"
    CLOTHES = "clothes"
    HAT = "hat"



class Products(BaseModel):
    id: int
    sku: str
    name: str
    price: float
    release_date: datetime
    category: Category