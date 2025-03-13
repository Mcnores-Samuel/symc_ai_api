"""Users model module, definition fo the user model for
database interactions
"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from core.db import Base
from uuid import uuid4


class User(Base):
    """User model class, user database presentaion"""
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid4, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    conversations = relationship(
        "Conversation", back_populates="user", cascade="all, delete-orphan")
