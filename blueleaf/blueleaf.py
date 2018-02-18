
import sys, os

from flask import Flask, render_template, render_template_string
import requests
import flask
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Bundle, Environment
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
import config

app = Flask(__name__, static_url_path='/static')
app.config.from_object(config.Config) # load config from this file

db = SQLAlchemy(app)
jsglue = JSGlue(app)

bundles = {
	'base_js': Bundle(
		'js/lib/jquery-3.3.1.min.js',
        'js/base.js',
        output='gen/base.js'
	),
    'base_css': Bundle(
        'css/lib/sierra.css',
        'css/base.scss',
        output='gen/base.css',
        depends=('css/incs/*.scss'),
        filters='pyscss'
    ),
    'login_js': Bundle(
        'js/login.js',
        output='gen/login.js',
    ),
    'login_css': Bundle(
        'css/login.scss',
        output='gen/login.css',
        filters='pyscss',
    ),
}
assets = Environment(app)
assets.auto_reload = True
assets.url = app.static_url_path
assets.config['PYSCSS_LOAD_PATHS'] = assets.load_path
assets.config['PYSCSS_STATIC_URL'] = assets.url
assets.config['PYSCSS_STATIC_ROOT'] = assets.directory
assets.config['PYSCSS_ASSETS_URL'] = assets.url
assets.config['PYSCSS_ASSETS_ROOT'] = assets.directory
assets.register(bundles)


# Define the User data-model.
# NB: Make sure to add flask_user UserMixin !!!
class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

        # User authentication information
        username = db.Column(db.String(100), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False, server_default='')
        email_confirmed_at = db.Column(db.DateTime())

        # User information
        first_name = db.Column(db.String(100), nullable=False, server_default='')
        last_name = db.Column(db.String(100), nullable=False, server_default='')

# Create all database tables
db.create_all()

# Setup Flask-User and specify the User data-model
db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
user_manager = UserManager(db_adapter, app)     # Initialize Flask-User

# The Home page is accessible to anyone
@app.route('/')
def home_page():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = flask.request.form
    return flask.json.jsonify({"success": True})

# The Members page is only accessible to authenticated users
@app.route('/members')
@login_required                                 # Use of @login_required decorator
def members_page():
	return render_template_string("""
    <h2> Not this</h2>
		""")



if __name__ == '__main__':
    app.run()
