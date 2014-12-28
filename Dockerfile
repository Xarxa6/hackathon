FROM ubuntu:14.04

EXPOSE 80

RUN apt-get update -y
RUN apt-get -y install python python-pip build-essential libpq-dev python-dev

ADD ./src /src
ADD requirements.txt /src/requirements.txt

RUN cd /src; pip install -r requirements.txt
RUN python -m nltk.downloader punkt stopwords maxent_treebank_pos_tagger

CMD ["python", "/src/init.py"]
