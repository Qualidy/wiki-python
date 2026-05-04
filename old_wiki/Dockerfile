
FROM python:3.11.7-bullseye

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen in das Arbeitsverzeichnis
COPY requirements.txt .

# Installiere die Anforderungen
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Projektcode in das Arbeitsverzeichnis
# COPY . :/app

# # Führe den Befehl "python mkdocs build" aus
# CMD ["mkdocs", "build"]

