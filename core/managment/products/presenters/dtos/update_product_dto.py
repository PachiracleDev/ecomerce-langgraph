from typing import List, Optional, Dict
from pydantic import Field, BaseModel

class UpdateProductDto(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=70)
    slug: Optional[str] = Field(None, min_length=3, max_length=255)
    description: Optional[str] = Field(None, min_length=3, max_length=255)
    price: Optional[float] = Field(None, gt=0)
    color: Optional[str] = Field(None, min_length=3, max_length=70)
    stock: Optional[int] = Field(None, gt=0)
    multimedia: Optional[List[dict]] = Field(None, min_items=1, max_items=5)  # lista de diccionarios
    sizes: Optional[Dict[str, List[str]]] = None  # diccionario con listas de tamaños
    category_id: Optional[int] = None