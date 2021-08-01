from flask import request 
from flask_restful import Resource
from database.models import db, User

class UserApi(Resource):
    # Get an user
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        return user.to_json(), 200

    # Update a user
    def put(self):
        body = request.get_json()
    
        user = User.query.filter_by(id=id).first()
        user.update(body)

        db.session.add(user)
        db.session.commit()
        return 'success', 204

    # Delete a user (only Admin)
    def delete(self):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        return 'success', 204

# Move create a user to autentication file
class UsersApi(Resource):
    pass

