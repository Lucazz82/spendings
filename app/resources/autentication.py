from werkzeug.wrappers.response import Response
from database.models import User, db
from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from werkzeug.exceptions import HTTPException

from .errors import (InvalidUsernameOrPassword, MissingRequiredArgument,
                     ServerError)


class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.query.filter_by(username=body['username']).one_or_none()

            if user is None:
                raise InvalidUsernameOrPassword

            if not user.check_password(body['password']):
                raise InvalidUsernameOrPassword

            token = create_access_token(identity=user.id)

            return make_response(jsonify(token=token, id=user.id), 200)

        except HTTPException as e:
            raise e
        except:
            raise ServerError


class RegisterApi(Resource):
    # Create a user
    def post(self):
        try:
            body = request.get_json()

            user = User(**body)

            db.session.add(user)
            db.session.commit()
            return {'id': user.id}, 201

        except HTTPException as e:
            raise e
        except TypeError as e:
            raise MissingRequiredArgument
        except:
            raise ServerError
