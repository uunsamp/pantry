from pantry.db import db

class Food(db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    amount = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Food %r>' % self.name
