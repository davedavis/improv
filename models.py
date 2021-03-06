from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import desc
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

# This needs to be added to work on the command line, avoiding the redefining of models.
# db.metadata.clear()


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(300))
    file_path = db.Column(db.String(264), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @staticmethod
    def newest(num):
        return Video.query.order_by(desc(Video.date)).limit(num)

    def __repr__(self):
        return "Bookmark '{}': '{}'>".format(self.description, self.url)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    videos = db.relationship('Video', backref='user', lazy='dynamic')
    password_hash = db.Column(db.String(256))

    @property
    def password(self):
        raise AttributeError('Password: Write Only Field. Check the models file if you are unsure')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    # ToDo: Add a get_userid_by_user

    def __repr__(self):
        return '<User %r>' % self.username
