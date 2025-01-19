from pydantic import BaseModel
from typing import Optional
from .models import User

class Token(BaseModel):
    access_token: str
    token_type: str
    user: User
    
class TokenData(BaseModel):
    username: Optional[str] = None

class UserInDB(BaseModel):
    db_hashed_password: str
