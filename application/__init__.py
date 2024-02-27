from flask import Flask

from application.main.routes import main

from .extensions import mongo

import os

def createapp():
    user = os.getenv("MONGO_USER")
    password = os.getenv("MONGO_PASSWORD")
    host = os.getenv("MONGO_HOST")
    db = os.getenv("MONGO_DB")
    app = Flask(__name__)

    app.config["MONGO_URI"] = "mongodb+srv://root:toor@recycle.uqnlrsp.mongodb.net/todos?retryWrites=true&w=majority&appName=Recycle"

    mongo.init_app(app)

    app.register_blueprint(main)
    return app







