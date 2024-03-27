from marshmallow import Schema, fields

class RecipeSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)
    first_name= fields.Str()
    last_name= fields.Str()

class PostSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str()
    body = fields.Str(required=True)
    author = fields.Int(required=True)