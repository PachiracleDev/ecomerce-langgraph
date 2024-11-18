from sqlalchemy.orm import Session
from core.auth.domain.user_schema import UserSchema
from core.auth.presenters.dtos.signin_dto import SigninDto
from shared.utils.bycript import verify_password
from shared.utils.jwt import create_access_token

def execute(session: Session, dto: SigninDto):
    user = session.query(UserSchema).filter(UserSchema.email == dto.email).first()
    if not user:
        raise ValueError('Credenciales incorrecta.')
    
    if not verify_password(dto.password, user.password):
        raise ValueError('Credenciales incorrecta.')
    
    # GENERATE_TOKEN
    
    token_data = {
        'user_id': user.id,
        'role': user.role
    }
    
    token = create_access_token(token_data)

    return {
        'token': token
    }
