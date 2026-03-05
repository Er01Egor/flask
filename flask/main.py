from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def fir(name0='title'):
    return render_template('index.html', title=name0)


@app.route('//<name_>')
def ind(name_='title'):
    return render_template('index.html', title=name_)

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



if __name__ == '__main__':
    app.run(port=8085, host='127.0.0.1')
