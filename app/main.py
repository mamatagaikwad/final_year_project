from fastapi import FastAPI, UploadFile, File, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List
import os, io, uuid, json
from PIL import Image

from .db import SessionLocal, engine, Base
from . import crud, dummy_model, models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

PRODUCT_MAP = {
    "acne": ["Acne Cleanser", "Salicylic Acid Serum"],
    "dark_spots": ["Vitamin C Serum", "Retinol Cream"],
    "eczema": ["Moisture Balm", "Oatmeal Lotion"],
    "redness": ["Niacinamide Serum", "Soothing Gel"],
    "healthy": ["Moisturizer", "Sunscreen SPF 50"]
}

@app.post("/api/analyze")
async def analyze(user_id: str = Form("guest"), files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    image_paths = []
    pil_images = []

    for f in files:
        data = await f.read()
        img = Image.open(io.BytesIO(data)).convert("RGB")

        processed = dummy_model.preprocess(img)
        pil_images.append(processed)

        filename = f"{uuid.uuid4().hex}_{f.filename}"
        save_path = os.path.join(UPLOAD_DIR, filename)
        img.save(save_path)

        image_paths.append(f"/uploads/{filename}")

    preds = dummy_model.predict(pil_images)
    products = []
    for p in preds:
        products += PRODUCT_MAP.get(p, [])

    record = crud.save_diagnosis(db, user_id, image_paths, preds, products)

    return {
        "id": record.id,
        "images": image_paths,
        "predicted_conditions": preds,
        "suggested_products": products
    }
