"""Conversations model module, definition fo the Conversation model for
database interactions
"""
from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from core.db import Base
from uuid import uuid4


class Conversations(Base):
    """Conversations model class, user database presentaion"""
    __tablename__ = "conversions"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid4, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True),
                     ForeignKey("users.id"), nullable=False)
    prompt = Column(String, nullable=False)
    response = Column(String, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="conversations")
