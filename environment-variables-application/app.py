from flask import Flask
import os

app = Flask(__name__)
env = os.getenv("APP_ENV", "dev")

@app.route("/")
def hello():
    return f"Environment is: {env}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
