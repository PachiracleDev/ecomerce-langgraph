from shared.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float,JSON
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total = Column(Float)
    status = Column(String, default='pending')
    delivery_id = Column(Integer, ForeignKey('deliveries.id'))
    order_items = Column(JSON, nullable=False)
    
    identifier = Column(String, nullable=False)

    user = relationship('User', back_populates='orders')
    
    delivery = relationship('Delivery', back_populates='orders')