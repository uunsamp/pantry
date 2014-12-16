from flask import Flask, jsonify
from pantry.models.food import Food
from pantry.db import create_db
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
create_db()
db.init_app(app)

@app.route('/food', methods=['GET'])
def list_food():
    child = items = []
    import ipdb; ipdb.set_trace()
    for food in Food.query.all():
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
