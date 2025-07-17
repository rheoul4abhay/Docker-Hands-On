from flask import Flask, request, render_template
app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

