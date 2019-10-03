FROM python:3

MAINTAINER itzhak cohen

COPY . /app

WORKDIR /app

RUN pip install Flask

CMD [ "python" , "app.py" ]
