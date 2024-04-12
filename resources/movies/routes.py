from flask import jsonify
from flask.views import MethodView
from flask_smorest import abort
from uuid import uuid4

from . import bp
from schemas import FilmSchema
from models.film_model import FilmModel

# from db import users, posts

@bp.route('/film')
class FilmList(MethodView):

    @bp.arguments(FilmSchema)
    def post(self, film_data):

        try:
            film = FilmModel()
            film.from_dict(film_data)

            film.save_post()

            return film
        except:
            abort(400, message=f"{film.title} failed to post")
    @bp.response(200, FilmSchema(many=True))
    def get(self):
        return FilmModel.query.all()

@bp.route('/post/<post_id>')
class Post(MethodView):

    @bp.response(200, FilmSchema)
    def get(self, post_id):
        try: 
            return FilmModel.query.get(post_id)
        except:
            abort(400, message="Post not found")

    @bp.arguments(FilmSchema)
    def put(self, film_data, film_id):
            
        print(film_data)
        film = FilmModel.query.get(film_id)
        if not film:
            abort(400, message="film not found")

        if film_data['film_id'] == film.film_id:
            og_film_id = film.film_id
            film.from_dict(film_data)
            film.user_id = og_film_id

            film.save_post()
            return film

    def delete(self, film_id):

        film = FilmModel.query.get(film_id)
        if not film:
            abort(400, message="film not found")
        
        film.del_post()
        return {'message': f'Film: {film_id} deleted'}, 200