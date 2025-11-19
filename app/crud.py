import json
from sqlalchemy.orm import Session
from .models import Diagnosis

def save_diagnosis(db: Session, user_id, paths, preds, products):
    diag = Diagnosis(
        user_id=user_id,
        images=json.dumps(paths),
        predicted_conditions=json.dumps(preds),
        suggested_products=json.dumps(products)
    )
    db.add(diag)
    db.commit()
    db.refresh(diag)
    return diag
