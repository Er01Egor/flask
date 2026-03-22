import datetime

from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_jobs():
    db_session.global_init("db/blogs.db")
    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = "deployment of residential modules 1 and 2"
    jobs.work_size = 15
    jobs.collaborators = "2, 3"
    jobs.start_date = datetime.datetime.now()
    jobs.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(jobs)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    add_jobs()