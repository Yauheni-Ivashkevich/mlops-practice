import os
from transformers import pipeline

MODEL_NAME = "bhadresh-savani/distilbert-base-uncased-emotion"
SAVE_PATH = "./model"

print(f"Скачивание модели {MODEL_NAME} с Hugging Face...")
# pipeline автоматически скачает модель из интернета
classifier = pipeline("text-classification", model=MODEL_NAME)
# Сохраняем веса и конфигурацию локально в папку ./model
classifier.save_pretrained(SAVE_PATH)
print(f"Модель успешно сохранена в папку {SAVE_PATH}")
