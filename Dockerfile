FROM python:3.7.7-alpine3.12

MAINTAINER Marcelo Aquino <marcelo.aquinojr7@gmail.com>

ADD . .

RUN apk add --no-cache --virtual .build-deps gcc linux-headers musl-dev && \ 
  python3 -m pip install -r requirements.txt --no-cache-dir

RUN ["chmod", "+x", "start-server.sh"]

EXPOSE 8181

CMD ["/start-server.sh"]
