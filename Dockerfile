FROM python:3

# Run Python in unbuffered mode so that outputs are not buffered 
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt 
RUN python3 -m pip install -r requirements.txt

RUN mkdir /urlshortener
WORKDIR /urlshortener
COPY . /urlshortener

COPY wait-for-it.sh /usr/wait-for-it.sh
RUN chmod +x /usr/wait-for-it.sh
