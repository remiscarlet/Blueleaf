from flask import Blueprint, json, render_template, redirect, url_for, request
from flask_user import login_required

home_blueprint = Blueprint('home', __name__,
                 template_folder='templates',
                 url_prefix='/home')

# The Home page is accessible to anyone

@home_blueprint.route('/')
@login_required
def home_page():
    return render_template('home.html')

