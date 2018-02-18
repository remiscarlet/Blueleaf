import flask
from flask import Blueprint, render_template

base = Blueprint('base', __name__,
                 template_folder='templates')

# The Home page is accessible to anyone
@base.route('/')
def home_page():
    return render_template('login.html')

@base.route('/login', methods=['GET', 'POST'])
def login():
	if flask.request.method == "GET":
		return redirect(url_for('/'))
	elif flask.request.method == "POST":
		data = flask.request.form
		if flask.request.form["email"] == "asdf":
			return flask.json.jsonify({"success": True})
		return flask.json.jsonify({"success": False}), 400
