# zato-web
# zato-web.py
# main file

# get flask
from flask import Flask
app = Flask(__name__)

# import modules from lib folder
from lib import database

@app.route("/")
def index():
    return "<h1>Coming Soon</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
