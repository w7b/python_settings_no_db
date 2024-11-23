FROM python:3

WORKDIR /app
EXPOSE 8085
COPY ./requirements.txt /tmp/requirements.txt
COPY . .

RUN pip install -U pip && pip install -r /tmp/requirements.txt


CMD ["python", "app/main.py"]