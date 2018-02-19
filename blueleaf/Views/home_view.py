from flask import Blueprint, json, render_template, redirect, url_for, request


home_blueprint = Blueprint('home', __name__,
                 template_folder='templates',
                 url_prefix='/home')

# The Home page is accessible to anyone
@home_blueprint.route('/')
def home_page():
    return render_template('home.html')

@home_blueprint.route('/loginaaaa', methods=['GET', 'POST'])
def login():
    from blueleaf import app
    app.logger.info("Hitting login endpoint")

    if request.method == "GET":
        return redirect(url_for('base.home_page'))

    elif request.method == "POST":
        data = request.form
        if request.form["email"] == "asdf":
            return json.jsonify({"success": True}), 200
        return json.jsonify({"success": False}), 400

