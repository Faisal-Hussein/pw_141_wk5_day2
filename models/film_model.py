from app import db


class FilmModel(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False, unique = True)
    creator = db.Column(db.String, nullable = False)
    genre = db.Column(db.String, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    def save_movie(self):
        db.session.add(self)
        db.session.commit()
    
    def del_movie(self):
        db.session.delete(self)
        db.session.commit()