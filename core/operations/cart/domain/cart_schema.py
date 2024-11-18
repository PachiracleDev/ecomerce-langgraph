from shared.db.database import Base
from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship


class CartSchema(Base):
    
    __tablename__ = 'carts'
    
    id: int = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, server_default='now()')
    products = relationship('CartItemSchema', back_populates='cart')
    
    