FROM continuumio/anaconda3:2021.11

COPY . /

WORKDIR .

ENTRYPOINT ["python", "main.py"]
