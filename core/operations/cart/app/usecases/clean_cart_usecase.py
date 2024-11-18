from sqlalchemy.orm import Session
from core.operations.cart.domain.cart_schema import CartSchema
from core.operations.cart.domain.cart_item_schema import CartItemSchema

def execute(session: Session, user_id: int):
    cart = session.query(CartSchema).filter(CartSchema.user_id == user_id).first()
    session.query(CartItemSchema).filter(CartItemSchema.cart_id == cart.id).delete()
    
    session.commit()
    
    return []