This project uses mongo and python, docker images

Step 1: Start the mongo server
  
    >> docker container run --name mongo-app --rm -p 27017:27017 -d mongo
  
Step 2: Insert some data in database
  
    >> docker exec -it mongo-app bash
      >> mongo
        >> use shubham
        >> db.createCollection("skt")
        >> db.skt.insert({"name":"shbhmtwr19"})
        >> exit
      >> exit

Step 3: Write the Dockerfile for flask application
    
    FROM python:3

    RUN pip install flask
    RUN pip install pymongo

    WORKDIR /usr/src/app

    COPY app.py .

    EXPOSE 5000
    CMD ["python","app.py"] 

Step 4: Write the app.py 
    
    from flask import Flask
    from pymongo import MongoClient
    import json

    app = Flask(__name__)

    client = MongoClient('172.17.0.2',27017) # this you get from command ">> docker inspect mongo-app""

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

Step 5: Build the image for flask application 
  
    >> docker bild . -t flask
  
Step 6: Run the container of the image we build just above

    >> docker container run --name flask-app --rm -p 5000:5000 --link mongo-app flask
  
Step 7: You are good to go.......
