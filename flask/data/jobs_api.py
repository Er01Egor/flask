import flask

from . import db_session
from .jobs import Jobs
from flask import jsonify, make_response, request

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'collaborators', 'job', 'work_size', 'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def one_jobs(job_id):
    db_sess = db_session.create_session()
    job = db_sess.get(Jobs, job_id)
    return jsonify(
        {
            'jobs': job.to_dict(only=(
                'team_leader', 'collaborators', 'job', 'work_size', 'is_finished'))
        }
    )
