FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-catche-dir-- -r requirements.txt

COPY . .

EXPOSE 5000

copy requirements.txt .

RUN pytest test_app.py -v

CMD ["python","app.py"]
