from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, ValidationError, Length, Regexp, EqualTo, Email

from models import User


class VideoUploadForm(FlaskForm):
    url = URLField('Please enter a URL')
    description = StringField('Add an optional description')
    file = FileField("Test", validators=[FileRequired()])


class LoginForm(FlaskForm):
    username = StringField('Your Username:', validators=[DataRequired()])
    password = PasswordField('Your Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(3, 80),
                                                   Regexp('^[A-Za-z0-9_]{3,}$',
                                                          message="Usernames can only be letters, numbers or underscores")])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(4, 99),
                                                     EqualTo('password2', message="Passwords must match")])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(),
                                                     Length(1, 120),
                                                     Email()])

    # ToDo: Figure our a better way of doing this that's not a static method (Or add decorator)
    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('There is already a user on this site with that email address')

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username is already taken by somebody else. Sorry!')

# Todo: Add video file validation.
# ToDo: Append username to filename to avoid duplicates and overwriting.
