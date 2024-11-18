from sqlalchemy.orm import Session
from core.auth.domain.user_schema import UserSchema
from core.operations.cart.domain.cart_schema import CartSchema
from core.auth.presenters.dtos.signup_dto import SignupDto
from shared.utils.bycript import get_password_hash
from shared.utils.jwt import create_access_token
from fastapi import HTTPException

def execute(session: Session, dto: SignupDto):
    try:
   
        #VERIFICAR SI EL EMAIL YA EXISTE
        user = session.query(UserSchema).filter(UserSchema.email == dto.email).first()
        if user:
            raise ValueError(f'El correo {dto.email} ya está en uso.')
        
        #HASH PASSWORD
        password_hash = get_password_hash(dto.password)
        
        user = UserSchema(
            name=dto.name,
            email=dto.email,
            password=password_hash,
            phone=dto.phone,
            gender=dto.gender
        )
        
        
        session.add(user)
        session.commit()
        
        cart = CartSchema(
            user_id=user.id
        )
        
        session.add(cart)
        session.commit()

        # GENERATE_TOKEN
        token_data = {
            'user_id': user.id,
            'role': user.role
        }
    
        token = create_access_token(token_data)

        return {
            'token': token
        }

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400,detail=str(e))
