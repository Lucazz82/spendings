from werkzeug.exceptions import HTTPException, NotFound
from database.models import User, db
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from .errors import ServerError


class UserApi(Resource):
    # Get an user
    @jwt_required()
    def get(self, id):
        try:
            user = User.query.filter_by(id=id).one_or_none()

            if user is None:
                raise NotFound

            return user.to_json(), 200
            
        except HTTPException as e:
            raise e
        except:
            raise ServerError

    # Update a user
    @jwt_required()
    def put(self, id):
        try:
            body = request.get_json()
        
            user = User.query.filter_by(id=id).one_or_none()

            if user is None:
                raise NotFound

            user.update(body)

            db.session.add(user)
            db.session.commit()
            return 'success', 204

        except HTTPException as e:
            raise e
        except:
            raise ServerError

    # Delete a user (only Admin)
    @jwt_required()
    def delete(self, id):
        try:
            user = User.query.filter_by(id=id).one_or_none()

            if user is None:
                raise NotFound
                
            db.session.delete(user)
            db.session.commit()

            return 'success', 204
        except HTTPException as e:
            raise e
        except:
            raise ServerError



