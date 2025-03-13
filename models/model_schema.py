from pydantic import BaseModel, EmailStr
import uuid
from datetime import datetime


class User(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    password: str
    created_at: datetime


class Conversation(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    prompt: str
    response: str
    timestamp: datetime
