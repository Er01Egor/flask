from flask import Flask, url_for, render_template, redirect

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


if __name__ == '__main__':
    app.run(port=8085, host='127.0.0.1')
