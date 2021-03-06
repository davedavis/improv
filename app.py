from flask import Flask
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin


app = Flask(__name__)

# App setup
# Store it in the apps config dict. This is needed for the flash function and and to access the session object.
app.config['SECRET_KEY'] = '\x83\xbf\x94\x19\x91\xd9:\x9a\x82\x12K\xbc\xa2\xc1f\xde\xc9\xbb\xa7\x82\xdd\t\xbb\xc7'

# SQLAlchemy setup.
# Suppress the annoying deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Local testing so it's OK for this to be on GitHub.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://thermos:thermosdev@localhost/improv'
db = SQLAlchemy(app)

# Admin Setup. Models need to be imported here after the DB is instantiated as models uses DB.
import models
app.config['FLASK_ADMIN_SWATCH'] = 'slate'
admin = Admin(app, name='improv', template_mode='bootstrap3')
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Video, db.session))


# Login/Authentication setup
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

# Needs to go at the end to avoid circular import issues.
import views, models
