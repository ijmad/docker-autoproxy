FROM ubuntu:latest
WORKDIR /app
EXPOSE 8080

RUN apt-get update && apt-get install -y python python-pip
ADD app /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD /app/proxyconfig.py
