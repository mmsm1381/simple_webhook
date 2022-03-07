FROM python:3.8.3-alpine 

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]