from app import app, db
from flask_script import Manager, prompt_bool
from models import User

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="Dave", email="dave@dave.com", password="dave"))
    db.session.add(User(username="Sarah", email="sarahe@sarah.com", password="dave"))
    db.session.commit()
    print('Initialized the DB')


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to drop everything?"):
        db.drop_all()
        print('Dropped the entire Database!')


if __name__ == '__main__':
    manager.run()
