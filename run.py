from flask import Flask, jsonify
from pantry.models.food import Food
from pantry.db import engine, init_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

init_db()

@app.route('/food', methods=['GET'])
def list_food():
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    session = Session()

    child = items = []
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
