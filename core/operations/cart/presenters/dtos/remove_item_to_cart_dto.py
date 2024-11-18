from pydantic import BaseModel

class RemoveItemToCartDto(BaseModel):
    item_id: int