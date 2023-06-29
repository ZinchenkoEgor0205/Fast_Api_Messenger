FROM python:3.11

RUN mkdir /fast_api_chat

WORKDIR /fast_api_chat

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
