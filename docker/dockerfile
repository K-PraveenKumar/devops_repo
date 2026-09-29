FROM python:3.12-slim

WORKDIR /django_fitness

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY manage.py .
COPY core ./core
COPY django_fitness ./django_fitness
COPY db.sqlite3 .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]