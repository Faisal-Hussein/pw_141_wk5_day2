from flask import request
from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort

from schemas import UserSchema
from . import bp

#from db import users
from models.user_model import UserModel

@bp.route('/user')
class UserList(MethodView):
    
    @bp.response(200, UserSchema)
    def get(self):
        return UserModel.query.all()

    
    @bp.arguments(UserSchema)
    @bp.response(201, UserSchema)
    def post(self, data):
        try:
            user = UserModel()
            user.from_dict(data)
            user.save_user()
            return user
        except:
            abort(400, message="username or email already taken, please try a different one!")

        
@bp.route('/user/<int:id>')
class User(MethodView):
    
    @bp.response(200, UserSchema)
    def get(self, id):
        user = UserModel.query.get(id)
        if user:
            return user
        else:
            abort(400, message="not a valid user")


    @bp.arguments(UserSchema)
    @bp.response(200, UserSchema)
    def put(self, data, id):
        user = UserModel.query.get(id)
        if user:
            user.from_dict(data)
            user.save_user()
            return user
        else:
            abort(400, message="not a valid user")          


    def delete(self, id):
        user = UserModel.query.get(id)
        if user:
            user.del_user()
            return { "message": "user GONE GONE GONE"}, 200
        abort(400, message="not a valid user")