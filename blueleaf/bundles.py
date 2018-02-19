from flask_assets import Bundle, Environment

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
    'flask-user_js': Bundle(
        'js/flask-user.js',
        output='gen/flask-user.js',
    ),
    'unauthenticated_css': Bundle(
        'css/unauthenticated.scss',
        'css/login.scss',
        'css/register.scss',
        output='gen/unauthenticated.css',
        filters='pyscss',
    ),
}
assets = Environment()
assets.auto_reload = True
assets.register(bundles)
