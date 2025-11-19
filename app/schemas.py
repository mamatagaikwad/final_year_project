from pydantic import BaseModel
from typing import List

class DiagnosisOut(BaseModel):
    id: int
    user_id: str | None
    images: List[str]
    predicted_conditions: List[str]
    suggested_products: List[str]

    class Config:
        orm_mode = True
