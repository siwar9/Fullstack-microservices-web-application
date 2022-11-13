FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /assignment
WORKDIR /assignment
COPY requirements.txt /assignment/
RUN pip install -r requirements.txt
COPY . /assignment/
CMD python run.py
#CMD gunicorn -w 3 --bind 0.0.0.0:5000 run:app