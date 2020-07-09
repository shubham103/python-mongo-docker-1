FROM python:3

RUN pip install flask
RUN pip install pymongo

WORKDIR /usr/src/app

COPY app.py .

EXPOSE 5000
CMD ["python","app.py"]
