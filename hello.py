from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    msg = f"Hello World from! {os.getenv('env')}"
    print(msg)
    return msg