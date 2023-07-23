FROM python:3.11.3-slim AS bot

WORKDIR /usr/src/app

COPY . .
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r ./requirements.txt

RUN chmod +x ./app/bot.py

CMD python3 ./app/bot.py;