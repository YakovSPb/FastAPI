FROM python:3.12.8

WORKDIR /app

COPY . .

RUN pip install -r requiments.txt


CMD ["python", "main.py"]