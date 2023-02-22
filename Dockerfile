FROM python:3.10

RUN pip install -U pipenv
RUN pipenv install

WORKDIR /Project/src

COPY . /Project

CMD ["pipenv", "run", "python", "assistant.py"]
