from shared.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship



class CartItemSchema(Base):
    
    __tablename__ = 'cart_items'
    
    id: int = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    
    #JSON {"short": "S", "polo": "L"}
    sizes = Column(JSON)
    
    cart = relationship('CartSchema', back_populates='products')
    products = relationship('Product')