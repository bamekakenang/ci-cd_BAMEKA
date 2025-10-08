<<<<<<< HEAD
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
# Image légère Python
FROM python:3.11-slim

# Empêcher Python d'écrire des bytecode pyc et bufferiser stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Créer l'utilisateur non-root
RUN useradd -m appuser
WORKDIR /app

# Installer dépendances système minimales
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installer dépendances Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code
COPY app ./app

# Exposer le port par défaut FastAPI
EXPOSE 8000

# Lancer l'API
USER appuser
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> 19c9cfa (Init CI/CD: app FastAPI, tests, Docker, workflows)
