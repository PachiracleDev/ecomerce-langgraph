from sqlalchemy.orm import Session
from core.operations.cart.domain.cart_schema import CartSchema
from core.operations.cart.domain.cart_item_schema import CartItemSchema

def execute(session: Session, user_id: int, item_id: int):
    cart = session.query(CartSchema).filter(CartSchema.user_id == user_id).first()
    cart_item = session.query(CartItemSchema).filter(CartItemSchema.cart_id == cart.id, CartItemSchema.id == item_id).first()
    session.delete(cart_item)
    session.commit()
    
    return cart_item