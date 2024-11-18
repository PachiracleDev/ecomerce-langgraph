
from core.operations.cart.presenters.dtos.update_item_cart_dto import UpdateItemCartDto

from sqlalchemy.orm import Session
from core.operations.cart.domain.cart_schema import CartSchema
from core.operations.cart.domain.cart_item_schema import CartItemSchema

def execute(session: Session, user_id: int, dto: UpdateItemCartDto):
    cart = session.query(CartSchema).filter(CartSchema.user_id == user_id).first()

    cart_item = session.query(CartItemSchema).filter(CartItemSchema.cart_id == cart.id, CartItemSchema.id == dto.item_id).first()
    
    
    if(dto.quantity):
       cart_item.quantity = dto.quantity
    
    if(dto.sizes):
       cart_item.sizes = dto.sizes
    
    session.commit()
    
    return cart_item
  