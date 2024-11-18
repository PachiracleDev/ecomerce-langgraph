from shared.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class UserSchema(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="user")