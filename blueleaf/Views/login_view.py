from flask import Blueprint, json, render_template, redirect, url_for, request


base_blueprint = Blueprint('base', __name__,
                 template_folder='templates')

# The Home page is accessible to anyone
@base_blueprint.route('/')
def home_page():
    return render_template('login.html')

@base_blueprint.route('/login', methods=['GET', 'POST'])
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

