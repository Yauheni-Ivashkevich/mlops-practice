import os
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification

MODEL_NAME = "bhadresh-savani/distilbert-base-uncased-emotion"
SAVE_PATH = "./model_onnx"

print(f"Скачивание и конвертация модели {MODEL_NAME} в ONNX...")

# Скачиваем токенизатор (он превращает текст в числа)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.save_pretrained(SAVE_PATH)

# Скачиваем модель и принудительно конвертируем её в ONNX граф
model = ORTModelForSequenceClassification.from_pretrained(MODEL_NAME, export=True)
model.save_pretrained(SAVE_PATH)

print(f"Оптимизированная ONNX модель сохранена в {SAVE_PATH}")
