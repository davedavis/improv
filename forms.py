from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url


class BookmarkForm(FlaskForm):
    url = URLField('Please enter a URL')
    description = StringField('Add an optional description')
    file = FileField("Test", validators=[FileRequired()])


class LoginForm(FlaskForm):
    username = StringField('Your Username:', validators=[DataRequired()])
    password = PasswordField('Your Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


# Todo: Add video file validation.
# ToDo: Append username to filename to avoid duplicates and overwriting.
