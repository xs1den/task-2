from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = {}  # ������� ��� ��������� ��������

class Item(Resource):
    def get(self, name):
        item = items.get(name)
        return (item, 200) if item else ({"message": "������� �� ��������"}, 404)

    def post(self, name):
        if name in items:
            return {"message": "������� ��� ����"}, 400
        data = request.get_json()
        item = {"name": name, "price": data.get("price")}
        items[name] = item
        return item, 201

    def put(self, name):
        data = request.get_json()
        item = {"name": name, "price": data.get("price")}
        items[name] = item
        return item, 200

    def delete(self, name):
        if items.pop(name, None):
            return {"message": "������� ��������"}, 200
        return {"message": "������� �� ��������"}, 404

# ������ ������ �� API
api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)

