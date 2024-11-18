from pydantic import BaseModel, Field

class UpdateUserBillingDto(BaseModel):
    address: str = None
    department: str = None
    city: str = None
    longitude: str  = None
    latitude: str = None
    agency: str = None