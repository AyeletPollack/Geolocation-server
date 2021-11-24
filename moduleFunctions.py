import requests
from mongoMethods import *

def is_open():
    try:
        check_connection()
    except Exception as ex:
        raise Exception(ex)


def get_distance_from_api(source,destination):
    url = 'https://www.mapquestapi.com/directions/v2/route?'
    response = requests.get(url + '&key=' + 'WrpxFLt5PZa7hQHLBZr1TBMsFjFAzlN3' + '&from=' + source + '&to=' + destination)
    return response.json()['route']['distance']


def get_most_popular():
    try:
        is_open()
        return find_max_hits()

    except Exception as ex:
        raise Exception(ex)


def get_distance_(source, destination):
    try:
        is_open()
        dbResponse = get_location(source, destination)
        if dbResponse != []:
            update_hits(dbResponse[0]["_id"], int(dbResponse[0]["hits"]))
            return dbResponse[0]["distance"]
        else:
            numberOfKMs = get_distance_from_api(source, destination)
            insert_to_db(source, destination, numberOfKMs, False)
            return numberOfKMs
    except Exception as ex:
        raise Exception(ex)


def insert_to_db(source, destination, numberOfKMs, check_exists):
    if not check_exists:
        insert(source, destination, numberOfKMs)
    else:
        dbResponse = get_location(source, destination)
        if dbResponse != []:
            update_distance(dbResponse[0]["_id"], numberOfKMs)
            return get_location(source, destination)[0]
        else:
            insert(source, destination, numberOfKMs)
        return get_location(source, destination)[0]
