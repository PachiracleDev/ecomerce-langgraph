from pydantic import BaseModel


class UserBilling(BaseModel):
    address: str
    department: str
    city: str
    longitude: str
    latitude: str
    agency: str