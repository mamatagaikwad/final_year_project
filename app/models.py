from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .db import Base

class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100))
    images = Column(Text)
    predicted_conditions = Column(Text)
    suggested_products = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
