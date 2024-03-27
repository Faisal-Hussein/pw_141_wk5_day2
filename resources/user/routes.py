from flask import Flask, request
from flask.views import MethodView
from uuid import uuid4

from schemas import RecipeSchema
from . import bp
from db import recipes

@bp.route('/user')
class UserList(MethodView):

    @bp.response(200, RecipeSchema(many=True))
    def get(self):
        return list(recipes.values())
    
    @bp.arguments(RecipeSchema)
    @bp.response(201, RecipeSchema)
    
    def post(self, data):
        recipe_id = uuid4().hex
        recipes[recipe_id] = data
        return recipes[recipe_id]
    
@bp.route('/user/<int:id>')
class User(MethodView):

    @bp.response(200, RecipeSchema)
    def get(self, id):
        if id in recipes:
            return recipes[id]
        return{
            'UH OH, something went wrong' :"Invalid recipe id"
        }, 400
    
    @bp.arguments(RecipeSchema)
    def put(self, data, id):
        data = request.get_json()
        if data[id] in recipes:
            recipes[data[id]] = data
            return {
                'recipe updated' : recipes[data[id]]
            }, 201
        return {
            'err' : 'no recipe found with that id'
        }, 401 
    
    def del_recipe(self, id):

        if id in recipes:
            del recipes[id]
            return { 'recipe gone': f" is no more. . . " }, 202
        return { 'err' : "can't delete that recipe, it isn't there. . . " } , 400
