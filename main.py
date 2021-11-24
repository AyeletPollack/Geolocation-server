import pymongo
from flask import Flask, request, Response
import requestes
import json

app = Flask(__name__)

@app.route('/home')
def get_home():
    return Response(status=200)

if __name__ == '__main__':
    app.run(prot=8080)

