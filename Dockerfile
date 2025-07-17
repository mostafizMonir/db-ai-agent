FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false"]
