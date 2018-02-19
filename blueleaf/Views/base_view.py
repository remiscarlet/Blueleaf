from flask import Blueprint, flash, json, render_template, redirect, url_for, request
from flask import current_app as app
from flask_user.views import _get_safe_next_param, _call_or_get
from flask_login import current_user, login_user, logout_user

base_blueprint = Blueprint('base', __name__,
                 template_folder='templates')

# The Home page is accessible to anyone
@base_blueprint.route('/')
def home_page():
    return redirect(url_for('base.login'))

@base_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    default_next = url_for('home.home_page')

    user_manager = app.user_manager
    db_adapter = user_manager.db_adapter

    safe_next = _get_safe_next_param('next', user_manager.after_login_endpoint)
    safe_reg_next = _get_safe_next_param('reg_next', user_manager.after_register_endpoint)

    app.logger.info("A")

    # Initialize form
    login_form = user_manager.login_form(request.form)          # for login.html
    register_form = user_manager.register_form()                # for login_or_register.html
    if request.method!='POST':
        login_form.next.data     = register_form.next.data     = safe_next
        login_form.reg_next.data = register_form.reg_next.data = safe_reg_next

    # If GET
    if request.method == "GET":
    # Immediately redirect already logged in users
        if _call_or_get(current_user.is_authenticated) and user_manager.auto_login_at_login:
            return redirect(safe_next if safe_next else default_next)
        return render_template('login.html')

    app.logger.info("A")

    # If POST
    if request.method=='POST':
        email = request.form.get("email")
        password = request.form.get('password')
        remember_me = False #request.form.get('remember_me');

        app.logger.info("A")
        user, user_email = user_manager.find_user_by_email(email)
        if user and user_manager.verify_password(password, user):
            app.logger.info("LOGGED IN???")
            login_user(user, remember=remember_me)

            #flash(_('You have signed in successfully.'), 'success')

            safe_next = user_manager.make_safe_url_function(login_form.next.data)

            return json.jsonify({'success': True, 'url':safe_next if safe_next else default_next}), 200

    return json.jsonify({'success': False}), 400

@base_blueprint.route('/logout', methods=['POST'])
def logout():
    """ Sign the user out."""
    default_next = url_for('base.login')
    user_manager =  app.user_manager

    # Use Flask-Login to sign out user
    logout_user()

    # Redirect to logout_next endpoint or '/'
    safe_next = _get_safe_next_param('next', user_manager.after_logout_endpoint)
    app.logger.info(safe_next if safe_next else default_next)
    return json.jsonify({'success': True, 'url':safe_next if safe_next else default_next}), 200

