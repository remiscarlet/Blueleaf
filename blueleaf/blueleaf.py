
import sys, os

from flask import Flask, render_template, render_template_string
import requests
import flask
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Bundle, Environment
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
import views
import models
import bundles
import config

# Base init
app = Flask(__name__, static_url_path='/static')
app.config.from_object(config.Config) # load config from this file

# Blueprints
app.register_blueprint(views.base)

# SQLAlchemy
db = models.db
db.app = app
db.init_app(app)

# JSGlue
jsglue = JSGlue(app)

# Bundles
assets = bundles.assets
assets.app = app
assets.init_app(app)
assets.url = app.static_url_path
assets.config['PYSCSS_LOAD_PATHS'] = assets.load_path
assets.config['PYSCSS_STATIC_URL'] = assets.url
assets.config['PYSCSS_STATIC_ROOT'] = assets.directory
assets.config['PYSCSS_ASSETS_URL'] = assets.url
assets.config['PYSCSS_ASSETS_ROOT'] = assets.directory

# Create all database tables
db.create_all()

# Setup Flask-User and specify the User data-model
db_adapter = SQLAlchemyAdapter(db, models.User)        # Register the User model
user_manager = UserManager(db_adapter, app)     # Initialize Flask-User

if __name__ == '__main__':
    app.run()
