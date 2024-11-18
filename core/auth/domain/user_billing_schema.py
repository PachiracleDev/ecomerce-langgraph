from shared.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
 

class UserBillingSchema(Base):
    
    __tablename__ = 'user_billing'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    address = Column(String, nullable=True)
    department = Column(String, nullable=True)
    city = Column(String, nullable=True)
    agency  = Column(String, nullable=True)
    
    longitude = Column(String, nullable=True)
    latitude = Column(String, nullable=True)
    
    country = Column(String, default='PE')
    
    
    