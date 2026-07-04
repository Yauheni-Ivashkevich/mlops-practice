# --- Этап 1: Скачивание модели и установка зависимостей ---
FROM python:3.10-slim AS builder

WORKDIR /build

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем библиотеки (флаг --no-cache-dir экономит место)
RUN pip install --no-cache-dir -r requirements.txt

# Копируем скрипт скачивания и запускаем его
COPY download_model.py .
RUN python download_model.py

# --- Этап 2: Финальный образ для продакшена ---
FROM python:3.10-slim AS runner

WORKDIR /app

# Копируем только установленные библиотеки из этапа builder в чистый образ
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Копируем скачанную модель и код нашего API
COPY --from=builder /build/model ./model
COPY app.py .

# Указываем порт, который приложение слушает внутри контейнера
EXPOSE 8000

# Команда для запуска нашего FastAPI приложения при старте контейнера
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
