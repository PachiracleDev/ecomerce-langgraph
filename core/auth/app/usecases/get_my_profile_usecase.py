from sqlalchemy.orm import Session
from core.auth.domain.user_schema import UserSchema
from fastapi import HTTPException

def execute(session: Session, user_id: int):
    user = session.query(UserSchema).filter(UserSchema.id == user_id).first()
    if not user:
        raise HTTPException(status_code=403,detail='Usuario no encontrado.')
    
    del user.password
    
    return user.__dict__
