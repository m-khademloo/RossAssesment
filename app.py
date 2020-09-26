from bson import ObjectId
from bson.json_util import dumps
from flask import Flask, request
from pymongo import MongoClient

from PaginationHelpers import get_pagination_parameters_from_http_context

app = Flask(__name__)

mongo_client = MongoClient('localhost', 27017)
db = mongo_client["SilkStartDb"]
collection = db["User"]


@app.route("/")
def get_api_info():
    welcome_message = {
        'apiVersion': 1,
        'status': 200,
        'message': 'Ross APIs - Managing Users'
    }
    return welcome_message


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    page, page_size = get_pagination_parameters_from_http_context(request)

    query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in request.args.items()}

    users = collection \
        .find(query, {'First Name': 1, 'last_name': 1}) \
        .skip((page - 1) * page_size) \
        .limit(page_size)

    if users.count() > 0:
        return dumps(users)
    else:
        return "", 204


@app.route("/api/v1/users/<user_id>", methods=['GET'])
def delete_user(user_id):
    try:
        found_users = collection.find({'_id': ObjectId(user_id)})
        if found_users.count() > 0:
            return dumps(found_users)
        else:
            return "Not Found", 404
    except:
        return "Not Found", 404  # in the case of wrong ID or anything else, we don't have the entity to response


if __name__ == '__main__':
    app.run()
