FROM python:3.9.6-alpine

EXPOSE 8080

COPY ./ /app

VOLUME [ "/app" ]

WORKDIR /app

RUN apk update
RUN apk add git
RUN pip install -r requirements.txt

CMD ["python", "-m", "src.main"]