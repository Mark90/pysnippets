FROM python:3.6

ENV PYTHONPATH /app

WORKDIR ${PYTHONPATH}

COPY requirements.txt ${PYTHONPATH}

RUN pip install -r requirements.txt
