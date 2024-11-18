from pydantic import BaseModel

class UpdateItemCartDto(BaseModel):
    quantity: int = None
    item_id: int 
    sizes: dict = None