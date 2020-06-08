from flask import Flask, render_template, redirect, url_for
from werkzeug.utils import secure_filename

import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = '\x83\xbf\x94\x19\x91\xd9:\x9a\x82\x12K\xbc\xa2\xc1f\xde\xc9\xbb\xa7\x82\xdd\t\xbb\xc7'


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = forms.VideoUploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/' + filename)
        return redirect(url_for('upload'))

    return render_template('upload.html', form=form)


if __name__ == '__main__':
    app.run()
