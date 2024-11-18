from shared.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

class Delivery(Base):
    __tablename__ = "deliveries"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))

    district = Column(String)
    province = Column(String)
    address = Column(String, nullable=True)
    
    # EN CASO SEA DE LIMA METROPOLITANA
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)
    
    # EN CASO SEA DE PROVINCIA
    agency = Column(String,  nullable=True)
    customer_name = Column(String, nullable=True)
    customer_document = Column(String, nullable=True)
    
    
    country = Column(String, default='Perú')
    
    orders = relationship('Order', back_populates='delivery')
    