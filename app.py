import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="MLOps Practice: Emotion Classifier")

# Указываем путь к папке с моделью, которую мы скачаем при сборке образа
MODEL_PATH = os.getenv("MODEL_PATH", "./model")

print("Загрузка модели в память приложения...")
# Инициализируем модель из ЛОКАЛЬНОЙ папки, а не из интернета
classifier = pipeline("text-classification", model=MODEL_PATH)
print("Модель готова к инференсу!")

# Описываем структуру входящего JSON-запроса
class TextRequest(BaseModel):
    text: str

# Эндпоинт для проверки работоспособности (Health Check)
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Эндпоинт для классификации
@app.post("/classify")
def classify_text(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Текст не может быть пустым")
    
    # Прогоняем текст через нейросеть
    result = classifier(request.text)
    
    return {
        "text": request.text,
        "label": result[0]["label"],
        "score": float(result[0]["score"])
    }
