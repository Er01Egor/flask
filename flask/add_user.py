import datetime

from flask import Flask
from data import db_session
from data.users import User

db_session.global_init("db/mars_explorer.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

data = [{'name': 'Ridley',
         'age': 21,
         'surname': 'Scott',
         'position': "captain",
         'email': 'scott_chief@mars.org',
         'speciality': 'research engineer',
         'address': 'module_1'},
        {'name': 'Sam',
         'age': 19,
         'surname': 'Smith',
         'position': "chief",
         'email': 'sam_durak@mars.org',
         'speciality': 'navigator',
         'address': 'module_1'},
        {'name': 'Dan',
         'age': 18,
         'surname': 'Williams',
         'position': "sailor",
         'email': 'williams_chief@mars.org',
         'speciality': 'boatswain',
         'address': 'module_3'},
        {'name': 'Jimmi',
         'age': 17,
         'surname': 'Brown',
         'position': "chief",
         'email': 'brown_chief@mars.org',
         'speciality': 'sailor',
         'address': 'module_4'}
        ]



def add_users():
    for elem in data:
        user = User()
        user.name = elem['name']
        user.age = elem['age']
        user.surname = elem['surname']
        user.position = elem['position']
        user.email = elem['email']
        user.speciality = elem['speciality']
        user.address = elem['address']
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()


if __name__ == '__main__':
    add_users()
