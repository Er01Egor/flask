
import json
import os
import random

from flask import Flask, url_for, render_template, redirect, request
from werkzeug.utils import secure_filename

from galeryform import UploadForm
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<name>')
@app.route('/index/<name>')
def index(name='title'):
    return render_template('index.html', title=name)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
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
    return render_template('login.html', title='Аварийный доступ', form=form)


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
    app.run(port=8087, host='127.0.0.1')
