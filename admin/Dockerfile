FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential python-mysqldb 
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
