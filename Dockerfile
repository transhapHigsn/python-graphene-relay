FROM ubuntu:latest

RUN apt-get clean && apt-get update -y \
    && apt-get install -y python3-dev build-essential

RUN apt-get install -y python3-pip
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]