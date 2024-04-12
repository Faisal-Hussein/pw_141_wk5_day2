from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)
    first_name= fields.Str()
    last_name= fields.Str()

class FilmSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    creator = fields.Str(required=True)
    genre = fields.Str(required=True)
    quantity = fields.Int(required=True)