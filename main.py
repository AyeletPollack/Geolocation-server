from flask import Flask, request, Response
import json
from mongoMethods import is_open
from mongoMethods import get_distance_
from mongoMethods import get_most_popular
from mongoMethods import insert_to_db


app = Flask(__name__)

######## API 1 ########
@app.route('/home', methods=['GET'])
def get_home():
    return Response(status=200)

######## API 2 ########
@app.route('/distance', methods=['GET'])
def get_distance():
    try:
        if(not(request.args.get('source'))):
            return Response(response=json.dumps({"message": "Please add source"}), status=400)
        if(not(request.args.get('destination'))):
            return Response(response=json.dumps({"message": "Please add destination"}), status=400)
        source = request.args.get('source')
        destination = request.args.get('destination')
        distance = get_distance_(source, destination)
        return Response(response=json.dumps({"distance": str(distance)}), status=200)

    except Exception as ex:
        print(str(ex))
        return Response(response=json.dumps({"message": str(ex)}), status=200)

######## API 3 ########
@app.route('/health')
def get_health():
    try:
        is_open()
        return Response(status=200)

    except Exception as ex:
        return Response(response=json.dumps({"message": ex}), status=500)

######## API 4 ########
@app.route('/popularsearch')
def get_popular_search():
    try:
        popular = get_most_popular()
        print(popular)
        if popular != {}:
            return Response(response=json.dumps({"source": popular["locationA"], "destination": popular["locationB"], "hits": popular["hits"]}), status=201)
        else:
            return Response(response=json.dumps({"message": "NO data in Data Base"}), status=201)

    except Exception as ex:
        return Response(response=json.dumps({"message": ex}), status=500)

######## API 5 ########
@app.route('/distance', methods=["POST"])
def create_distance():
    try:
        if not (request.form.get("source")):
            return Response(response=json.dumps({"message": "Please add source"}), status=400)
        if not (request.form.get("destination")):
            return Response(response=json.dumps({"message": "Please add destination"}), status=400)
        if not (request.form.get("distance")):
            return Response(response=json.dumps({"message": "Please add distance"}), status=400)

        source = request.form["source"]
        destination = request.form["destination"]
        distance = request.form["distance"]
        popular = insert_to_db(source, destination, distance, True)

        return Response(response=json.dumps({"source": source, "destination": destination, "hits": popular["hits"]}), status=201)

    except Exception as ex:
        return Response(response=json.dumps({"message": ex}), status=500)


if __name__ == '__main__':
    app.run(port=8080)

