from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Scott2"
    user.name = "Ridley2"
    user.age = 35
    user.position = "captain2"
    user.speciality = "research engineer2"
    user.address = "module_2"
    user.email = "scott_chief2@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Scott3"
    user.name = "Ridley3"
    user.age = 27
    user.position = "captain3"
    user.speciality = "research engineer3"
    user.address = "module_3"
    user.email = "scott_chief3@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
