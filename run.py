from flask import Flask, jsonify
from pantry.models.food import Food
from pantry.db import Base, engine
from sqlalchemy.orm import sessionmaker
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# create the db
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_seed():
    session.add_all([
        Food(name='apple', amount=3),
        Food(name='banana', amount=4),
    ])
    session.commit()

# if seed data isn't in db, create it
if session.query(Food).count() < 0:
    create_seed()

@app.route('/food', methods=['GET'])
def list_food():
    child = items = []
    import ipdb; ipdb.set_trace()
    for food in session.query(Food):
        item = {
            "_id": food.id,
            "name": food.name,
            "amount": food.amount,
        }
        items.append(item)
    _links = {}
    _links["child"] = items
    response = {}
    response["_links"] = _links
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
