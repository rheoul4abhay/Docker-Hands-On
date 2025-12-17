from flask import Flask, request, jsonify
from tasks import reverse_string

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse():
    data = request.get_json()
    task = reverse_string.delay(data["text"])
    return jsonify({'task_id': task.id}), 202

