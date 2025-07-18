from flask import Flask, jsonify, request
import json, os

app = Flask(__name__)
DATA_FILE = 'data.json'

def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(read_data())

@app.route('/todos', methods=['POST'])
def add_todo():
    data = read_data()
    new_todo = request.get_json()
    new_todo["id"] = len(data) + 1
    data.append(new_todo)
    write_data(data)
    return jsonify(new_todo), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = read_data()
    for todo in data:
        if todo["id"] == id:
            todo.update(request.get_json())
            write_data(data)
            return jsonify(todo)
    return jsonify({"error": "Not found"}), 404

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    data = read_data()
    data = [todo for todo in data if todo["id"] != id]
    write_data(data)
    return jsonify({"message": "Deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

