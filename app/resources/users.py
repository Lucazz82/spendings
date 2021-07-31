from flask_restful import Resource
from databases.models import User

class UserApi(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        return user.to_json(), 200

    def post(self):
        body = request.get_json()
        # user = User(username=body['username'], hash=generate_password_hash(body['password']))
        user = User(**body)
        user.hash_password()

        db.session.add(user)
        db.session.commit()
        return {'id': user.id}, 201


class UsersApi(Resource):
    pass


class SpendingApi(Resource):
    pass


class SpendingsApi(Resource):
    pass

