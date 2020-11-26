import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Home
@app.route("/")
@app.route("/home")
def home():
    return "Hello, this is a test!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)