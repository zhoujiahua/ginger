#! /bin/usr/python3

from flask import Flask


def register_blueprints(app):
    from app.api.v1.user import user
    from app.api.v1.book import book
    app.register_blueprint(user)
    app.register_blueprint(book)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    return app
