from flask_restful import Resource
from flask import request, jsonify, make_response
from database.models import db, User
from flask_jwt_extended import create_access_token

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.query.filter_by(username=body['username']).one_or_none()

        if user is None:
            return make_response(jsonify({'msg': 'invalid username or password'}), 401)

        if not user.check_password(body['password']):
            return make_response(jsonify({'msg': 'invalid username or password'}), 401)

        token = create_access_token(identity=user.id)

        return make_response(jsonify(token=token, id=user.id), 200)


class RegisterApi(Resource):
    # Create a user
    def post(self):
        body = request.get_json()
        # user = User(username=body['username'], hash=generate_password_hash(body['password']))
        # user = User(**body)
        # user.hash_password()
        user = User()
        user.create_user(**body)

        db.session.add(user)
        db.session.commit()
        return {'id': user.id}, 201