from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url
from wtforms import PasswordField, BooleanField, SubmitField, StringField


class VideoUploadForm(FlaskForm):
    video_file = FileField(validators=[FileRequired()])
