from flask import request, jsonify, Response, make_response
from flask_restful import Resource
from database.models import db, Spending
from flask_jwt_extended import jwt_required

class SpendingApi(Resource):
    def get(self, user_id, spending_id):
        spending = Spending.query.filter_by(id = spending_id, user_id=user_id).first()

        return make_response(jsonify(spending.to_json()), 200)

    # Update spending
    def put(self, user_id, spending_id):
        body = request.get_json()
        spending = Spending.query.filter_by(id=spending_id, user_id=user_id).first()

        spending.update(body)

        db.session.add(spending)
        db.session.commit()

        return 'success', 204


    # Delete spending
    def delete(self, user_id, spending_id):
        spending = Spending.query.filter_by(id=spending_id, user_id=user_id).first()

        db.session.delete(spending)
        db.session.commit()

        return 'success', 204


class SpendingsApi(Resource):
    # Retrive all spendings from user
    @jwt_required()
    def get(self, user_id):
        spendings = Spending.query.filter_by(user_id=user_id)
        response = []

        for spending in spendings:
            response.append(spending.to_json())

        return make_response(jsonify(response), 200)
    
    # Add spending
    def post(self, user_id):
        body = request.get_json()
        spending = Spending(**body)
        spending.userId = user_id

        db.session.add(spending)
        db.session.commit()

        return {'id': spending.id}, 200