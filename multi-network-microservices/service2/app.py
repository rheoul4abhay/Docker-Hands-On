from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return "Hello from Service2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)
