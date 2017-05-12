FROM ubuntu:latest
WORKDIR /app
EXPOSE 8080

ENV SQUID_LOG_DIR=/var/log/squid

RUN apt-get update && apt-get install -y squid3

ADD squid.conf /app/squid.conf

CMD squid3 -s -d 1 -N -f /app/squid.conf
