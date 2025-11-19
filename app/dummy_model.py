import random

CONDITIONS = ["acne", "dark_spots", "eczema", "redness", "healthy"]

def preprocess(img):
    return img.resize((224,224))

def predict(images):
    results = [random.choice(CONDITIONS) for _ in images]
    ##machine learning ......provide prediction
    return list(set(results))[:2]
