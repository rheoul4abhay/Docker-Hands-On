from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    response = requests.get("http://service2:5051/")
    return f"Hello from Service1! Also got : {response.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
