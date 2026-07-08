# 🚀 Production-Ready Emotion Classifier API (MLOps Practice)

![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![Docker](https://img.shields.io/badge/docker-desktop-blue.svg)
![ONNX Runtime](https://img.shields.io/badge/ONNX-Runtime-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green.svg)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%20Passing-brightgreen.svg)

Высокооптимизированный микросервис для классификации эмоций в тексте на базе модели `DistilBERT`. Проект разработан в рамках методологии **MLOps** с упором на минимизацию потребления ресурсов (RAM), высокую скорость инференса и полную автоматизацию CI/CD пайплайна.

---

## 🛠 Технологический стек и архитектура

В данном проекте реализован сквозной пайплайн доставки ML-модели в продакшн:

* **Фреймворк:** FastAPI (асинхронный обработчик, автоматическая интерактивная документация Swagger UI).
* **Оптимизация:** Hugging Face `Optimum` + `ONNX Runtime`. Тяжелый граф вычислений PyTorch скомпилирован в легковесный бинарный формат, что позволило сократить время холодного старта и потребление памяти.
* **Контейнеризация:** Двухэтапная сборка (**Multi-stage Docker build**). Финальный образ содержит только легковесный рантайм и веса модели, полностью отсекая инструменты сборки и лишние зависимости тяжелого PyTorch.
* **Оркестрация:** Docker Compose для декларативного управления контейнерами и конфигурациями окружения.
* **Автоматизация (CI):** GitHub Actions. Автоматическая сборка, изоляция окружения и Health Check на удаленном сервере Ubuntu при каждом пуше в ветку `main`.

---

## ⚡ Быстрый запуск проекта

Для развертывания проекта на локальной машине необходим только установленный **Docker Desktop**.

### 1. Клонирование и переход в проект
```bash
git clone [https://github.com/Yauheni-Ivashkevich/mlops-practice.git](https://github.com/Yauheni-Ivashkevich/mlops-practice.git)
cd mlops-practice
