import dataset
from flask import Blueprint, jsonify
from loguru import logger
from marshmallow import pprint

from budget_dash.db import UserSchema, db

api = Blueprint("api", __name__, url_prefix="/api")


def J(*args, **kwargs):
    """Wrapper around jsonify that sets the Content-Type of the response to
    application/vnd.api+json.
    """
    response = jsonify(*args, **kwargs)
    response.mimetype = "application/vnd.api+json"
    return response


@api.route("/users/")
def users():
    users = db["users"].all()
    users_schema = UserSchema(many=True)
    result = users_schema.dump(users)
    return J(result)


@api.route("/user/<int:user_id>/")
def user(user_id):
    users = db["users"]
    user = users.find_one(id=user_id)
    schema = UserSchema()
    return J(schema.dump(user))
