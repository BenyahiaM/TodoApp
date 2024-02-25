from flask import Flask

from application.main.routes import main

from .extensions import mongo


def createapp():
    app = Flask(__name__)

    app.config["MONGO_URI"] = "mongodb+srv://root:toor@recycle.uqnlrsp.mongodb.net/todos?retryWrites=true&w=majority&appName=Recycle"

    mongo.init_app(app)

    app.register_blueprint(main)
    return app







