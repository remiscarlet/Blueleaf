
import sys, os

from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Bundle, Environment
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
import config

app = Flask(__name__, static_url_path='/static')
app.config.from_object(config.Config) # load config from this file

db = SQLAlchemy(app)

bundles = {
	'base_js': Bundle(
		'js/lib/jquery-3.3.1.min.js',
        'js/base.js',
        output='gen/base.js'
	),
    'base_css': Bundle(
        'css/base.scss',
        output='gen/base.css',
        filters='pyscss'
    ),
}
assets = Environment(app)
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
	return render_template_string("""
		{% extends "base.html" %}
		{% block content %}
			<h2>Home page</h2>
			<p>This page can be accessed by anyone.</p><br/>
			<p><a href={{ url_for('home_page') }}>Home page</a> (anyone)</p>
			<p><a href={{ url_for('members_page') }}>Members page</a> (login required)</p>
		{% endblock %}
		""")

# The Members page is only accessible to authenticated users
@app.route('/members')
@login_required                                 # Use of @login_required decorator
def members_page():
	return render_template_string("""
		{% extends "base.html" %}
		{% block content %}
			<h2>Members page</h2>
			<p>This page can only be accessed by authenticated users.</p><br/>
			<p><a href={{ url_for('home_page') }}>Home page</a> (anyone)</p>
			<p><a href={{ url_for('members_page') }}>Members page</a> (login required)</p>
		{% endblock %}
		""")

if __name__ == '__main__':
    app.run()
