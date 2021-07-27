FROM python:3.9.6-alpine

EXPOSE 8080

COPY ./ /app

VOLUME [ "/app" ]

WORKDIR /app

RUN apk update
RUN apk add git
RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]