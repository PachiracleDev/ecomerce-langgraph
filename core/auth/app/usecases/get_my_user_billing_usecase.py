from sqlalchemy.orm import Session
from core.auth.domain.user_billing_schema import UserBillingSchema
 

def execute(session: Session, user_id: int):
    user_billing = session.query(UserBillingSchema).filter(UserBillingSchema.user_id == user_id).first()
    if not user_billing:
        return {}
    
    return user_billing.__dict__
