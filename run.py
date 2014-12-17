from flask import Flask, jsonify
from pantry.models.food import Food
from pantry.db import db
from pantry.app import create_app
import json

app = create_app()

@app.route('/food', methods=['GET'])
def list_food():
    child = items = []
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
