import os

from flask import Flask, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from forms import UploadForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '\x83\xbf\x94\x19\x91\xd9:\x9a\x82\x12K\xbc\xa2\xc1f\xde\xc9\xbb\xa7\x82\xdd\t\xbb\xc7'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # Create a new instance of the Upload form.
    form = UploadForm()

    # If the form is POST, validate and save the file flashing a success message.
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        root_dir = os.path.dirname(app.instance_path)
        form.file.data.save(os.path.join(root_dir, 'uploads', filename))
        # ToDo: Submit to the YouTube API: https://developers.google.com/youtube/v3/guides/uploading_a_video
        flash("Received your file, thanks!")
        return redirect(url_for('upload'))
    # If it's a GET, render the form as normal.
    return render_template('upload.html', form=form)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
