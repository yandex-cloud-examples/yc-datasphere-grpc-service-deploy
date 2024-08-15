FROM cr.yandex/mirror/python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt

COPY . .

RUN make proto

CMD [ "python", "server.py" ]