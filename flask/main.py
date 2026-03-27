import os
from random import random

from flask import Flask, url_for, request, render_template, redirect, abort
from werkzeug.utils import secure_filename

from data import db_session
from data.users import User
from galeryform import UploadForm
from forms.user import RegisterForm
from forms.login import LoginForm
from flask_login import login_user
from flask_login import LoginManager, login_user
from flask_login import login_required, logout_user, current_user
import json
from flask import make_response

import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index(name='title'):
    return render_template('work_log.html', title=name)


@app.route('/suse')
def suse():
    return 'OK'


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data,

        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/distribution")
def distribution():
    user_list = ['Ваня', 'Петя', 'Саша', 'Кирилл']
    return render_template('index2.html', user_list=user_list)


@app.route('/training/<prof>')
def training(prof):
    return render_template('index3.html', prof=prof)


@app.route('/list_prof/<val>')
def marker(val):
    proffe = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
              "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения",
              "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    if val == "ul":
        return render_template('index4.html', proff=proffe)
    elif val == "ol":
        return render_template('index4.1.html', proff=proffe)
    else:
        return "Неверный ввод"


@app.route('/answer')
@app.route('/auto_answer')
def answ():
    pretedents = [
        {
            "title": "Анкета",
            "surname": "Starkkk",
            "name": "Mark",
            "education": "Выше среднего",
            "profession": "Штурман",
            "sex": "Муж",
            "motivation": "Всегда мечтал об этом",
            "ready": "Хочет домой"
        },
        {
            "title": "Анкета",
            "surname": "Ivanov",
            "name": "Yan",
            "education": "Основное",
            "profession": "Инженер",
            "sex": "Муж",
            "motivation": "мечтал об этом",
            "ready": " НЕ Хочет домой"
        },
        {
            "title": "Анкета",
            "surname": "Petrova",
            "name": "Margo",
            "education": "Выше среднего",
            "profession": "Командир",
            "sex": "Жен",
            "motivation": "Всегда  Не мечтал об этом",
            "ready": "Хочет домой"
        }
    ]
    answer = random.choice(pretedents)
    return render_template('answer.html', **answer)


@app.route('/login1', methods=['GET', 'POST'])
def login1():
    form = LoginForm()
    if form.validate_on_submit():
        id_avs = form.username_avs.data
        pass_avs = form.password_avs.data

        id_com = form.username_com.data
        pass_com = form.password_com.data

        print(f"ID Астронавта: {id_avs}")
        print(f"Пароль Астронавта: {pass_avs}")
        print(f"ID Капитана: {id_com}")
        print(f"Пароль Капитана: {pass_com}")
        return render_template('finish_log.html', title='Аварийный доступ')
    return render_template('login1.html', title='Аварийный доступ', form=form)


@app.route('/table/<pol>/<int:years>')
def table(pol, years):
    return render_template('table_cel.html', title='table', sex=pol, years=years)


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    form = UploadForm()
    img_name = request.args.get('data_img')
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/img', filename))
        return redirect(url_for('galery', data_img=filename))
    return render_template('galery.html', title='Красная планета', form=form, data_img=img_name)


@app.route('/member')
def member():
    with open('templates/members.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    answer = random.choice(data)
    return render_template('card.html', title='card', member_card=answer)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8000, host='127.0.0.1')
