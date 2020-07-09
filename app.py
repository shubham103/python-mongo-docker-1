from flask import Flask
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient('172.17.0.2',27017)  # ip address from command >>  docker inspect mongo-app

db = client.shubham

col= db.skt

names= col.find()

@app.route("/",methods=['GET'])
def index():
  documents = col.find()
  response = []
  for document in documents:
    document['_id'] = str(document['_id'])
    response.append(document)
  return json.dumps(response)
 

if __name__ == "__main__":
  app.run(host="0.0.0.0")

