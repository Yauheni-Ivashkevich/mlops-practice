import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForSequenceClassification

app = FastAPI(title="MLOps Practice: Optimized ONNX Classifier")

MODEL_PATH = os.getenv("MODEL_PATH", "./model_onnx")

print("Загрузка оптимизированной ONNX модели...")
# Загружаем модель через ONNX Runtime
model = ORTModelForSequenceClassification.from_pretrained(MODEL_PATH, provider="CPUExecutionProvider")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

# Создаем стандартный пайплайн, но уже на движке ONNX
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
print("ONNX модель готова к быстрому инференсу!")

class TextRequest(BaseModel):
    text: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/classify")
def classify_text(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Текст не может быть пустым")
    
    result = classifier(request.text)
    return {
        "text": request.text,
        "label": result[0]["label"],
        "score": float(result[0]["score"])
    }
