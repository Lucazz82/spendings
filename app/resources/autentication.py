from flask_restful import Resource
from flask import request, jsonify, make_response
from database.models import db, User
from flask_jwt_extended import create_access_token

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.query.filter_by(username=body['username']).first()

        if user is None:
            return make_response(jsonify({'msg': 'invalid username or password'}), 400)

        if not user.check_password(body['password']):
            return make_response(jsonify({'msg': 'invalid username or password'}), 400)

        token = create_access_token(identity=user.id)

        return make_response(jsonify(token), 200)


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