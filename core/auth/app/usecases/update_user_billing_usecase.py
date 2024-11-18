from sqlalchemy.orm import Session
from core.auth.domain.user_billing_schema import UserBillingSchema
from core.auth.presenters.dtos.update_user_billing_dto import UpdateUserBillingDto

def execute(session: Session, user_id: int, dto: UpdateUserBillingDto):
    user_billing = session.query(UserBillingSchema).filter(UserBillingSchema.user_id == user_id).first()
    if not user_billing:
        ## SE LE CREARA UN REGISTRO DE FACTURACION
        user_billing = UserBillingSchema(user_id=user_id, **dto.__dict__)
        session.add(user_billing)
        session.commit()
        return {
            "message": 'Registro de facturación creado con éxito'
        }
    
    update_data = {key: value for key, value in dto.__dict__.items() if value is not None}

    session.query(UserBillingSchema).filter(UserBillingSchema.user_id == user_id).update(update_data)
    session.commit()
    
    
    
    return {
        "message": 'Actualización de facturación actualizado con éxito'
    }
