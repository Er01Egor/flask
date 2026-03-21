from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db = input().split('.')
db_session.global_init("db/" + db[0] + ".db")
db_sess = db_session.create_session()
for user in db_sess.query(User).all():
    if user.address == 'module_1':
        print(user)
