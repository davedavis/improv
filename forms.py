from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired


class UploadForm(FlaskForm):
    file = FileField()

# Todo: Add video file validation.
# ToDo: Append username to filename to avoid duplicates and overwriting.
