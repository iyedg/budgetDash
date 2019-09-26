from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema
import dataset


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    email = fields.Email()

    class Meta:
        type_ = "user"
        self_view = "api.user"
        self_view_kwargs = {"user_id": "<id>"}
        self_view_many = "api.users"


db = dataset.connect("sqlite:///mydatabase.db")
