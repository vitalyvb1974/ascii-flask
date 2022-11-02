FROM continuumio/anaconda3:2021.11

COPY . /

WORKDIR /ascii-flask

ENTRYPOINT ["python", "main.py"]