# Используйте multi-stage сборку, если нужно:
FROM postgres:latest AS db
ENV POSTGRES_PASSWORD=90909090qQ
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
EXPOSE 5432

# Основной образ для Python
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
