from pydantic import BaseModel, Field
from typing import List

class Multimedia(BaseModel):
    url: str
    type: str

class ProductSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=70)
    slug: str = Field(..., min_length=3, max_length=255)
    description: str = Field(..., min_length=3, max_length=255)
    price: float = Field(..., gt=0)
    color: str = Field(..., min_length=3, max_length=70)
    stock: int = Field(..., gt=0)
    # Array JSON {"url": "https://www.google.com", "type": "video"} {"url": "https://www.google.com", "type": "image"}
    multimedia: List = Field(..., min_items=1, max_items=5)
    # #JSON  {"short": ["S", "M", "L"], "polo": ["S", "M", "L", "XL"]}
    sizes: dict
    category_id: int 