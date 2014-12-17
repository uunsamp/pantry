from pantry.db import db

class Food(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    amount = db.Column(db.Integer, unique=False)

    def __init__(self, app):

        def __init__(self, name, amount):
            self.name = name
            self.amount = amount

        def __repr__(self):
            return '<Food %r>' % self.name
