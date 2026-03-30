from flask import jsonify
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash
from . import db_session
from users import User
from reqparse_user import parser


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"Users {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.get(User, user_id)
        return jsonify({'user': user.to_dict(
            only=('name', 'surname', 'age', 'email', 'position', 'speciality', 'address', 'hashed_password'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.get(User, user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'news': [item.to_dict(
            only=('name', 'surname', 'age', 'email', 'position', 'speciality', 'address', 'hashed_password')) for item in user]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            email=args['email'],
            position = args['position'],
            speciality = args['speciality'],
            address=args['address'],
            hashed_password = args['hashed_password']

        )
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
