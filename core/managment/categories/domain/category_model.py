from shared.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    # Relación para obtener subcategorías
    subcategories = relationship('Category', backref='parent', remote_side=[id])
 
    products = relationship("Product", back_populates="category")
