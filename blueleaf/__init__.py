# -*- coding: UTF-8 -*-
import flask
from flask import Flask, render_template
from flask_jsglue import JSGlue
from flask_user import UserManager, SQLAlchemyAdapter

import sys, os
import requests

import logging
from logging.handlers import RotatingFileHandler

from .Views.base_view import base_blueprint
from .Views.home_view import home_blueprint
from .Models.user_model import user_db, User
from .bundles import assets
from .config import Config

# Base init
app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config) # load config from this file

handler = RotatingFileHandler(app.config["LOG_LOCATION"], maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Blueprints
app.register_blueprint(base_blueprint)
app.register_blueprint(home_blueprint)

# JSGlue
jsglue = JSGlue(app)

# Bundles
assets.app = app
assets.init_app(app)
assets.url = app.static_url_path
assets.config['PYSCSS_LOAD_PATHS'] = assets.load_path
assets.config['PYSCSS_STATIC_URL'] = assets.url
assets.config['PYSCSS_STATIC_ROOT'] = assets.directory
assets.config['PYSCSS_ASSETS_URL'] = assets.url
assets.config['PYSCSS_ASSETS_ROOT'] = assets.directory

# SQLAlchemy
user_db.app = app
user_db.init_app(app)

# Create all database tables
user_db.create_all()

# Setup Flask-User and specify the User data-model
db_adapter = SQLAlchemyAdapter(user_db, User)        # Register the User model
user_manager = UserManager(db_adapter, app)     # Initialize Flask-User

if __name__ == '__main__':
    app.run()
app.logger.info("AAAAAAAAAAAAAAA");
