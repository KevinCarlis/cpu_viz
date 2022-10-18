FROM python:3.8-slim-buster

ADD ./app /app
WORKDIR /app

ENV FLASK_APP=my_app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN make

EXPOSE 5000

CMD ["flask", "run"]
