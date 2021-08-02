from flask import request 
from flask_restful import Resource
from database.models import db, User
from flask_jwt_extended import jwt_required, get_jwt_identity

class UserApi(Resource):
    # Get an user
    @jwt_required()
    def get(self, id):
        user = User.query.filter_by(id=id).one_or_none()
        return user.to_json(), 200

    # Update a user
    @jwt_required()
    def put(self, id):
        body = request.get_json()
    
        user = User.query.filter_by(id=id).one_or_none()
        user.update(body)

        db.session.add(user)
        db.session.commit()
        return 'success', 204

    # Delete a user (only Admin)
    @jwt_required()
    def delete(self, id):
        user = User.query.filter_by(id=id).one_or_none()
        db.session.delete(user)
        db.session.commit()

        return 'success', 204



