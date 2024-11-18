from shared.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String)
    description = Column(String)
    price = Column(Integer)
    color = Column(String)
    stock = Column(Integer)
    
    #JSON {"url": "https://www.google.com", "type": "video"} {"url": "https://www.google.com", "type": "image"}
    multimedia = Column(JSON)
    
    #JSON  {"short": ["S", "M", "L"], "polo": ["S", "M", "L", "XL"]}
    sizes = Column(JSON)

    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship("Category", back_populates="products")
     