From python:3.8.1-alpine3.11

MAINTAINER Victor Biederbeck "james@jamesbiederbeck.com"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "devicetable.py" ]
