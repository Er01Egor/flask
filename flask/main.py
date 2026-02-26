from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/d')
def main():
    return "sajsdj"

@app.route('/')
@app.route('/index')
def index():
    print('dsf')
    return render_template('index.html', title='Заготовка')

if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')