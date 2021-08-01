from flask import request, jsonify, Response
from flask_restful import Resource
from database.models import db, Spending

class SpendingApi(Resource):
    def get(self, user_id, spending_id):
        spending = Spending.query.filter_by(id = spending_id, user_id=user_id).first()

        # Should put , 200 for response code but Exception raised
        return jsonify(spending.to_json())

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
    def get(self, user_id):
        spendings = Spending.query.filter_by(userId=user_id)
        response = []

        for spending in spendings:
            response.append(spending.to_json())

        # Should put , 200 for response code but Exception raised
        return jsonify(response)
    
    # Add spending
    def post(self, user_id):
        body = request.get_json()
        spending = Spending(**body)
        spending.userId = user_id

        db.session.add(spending)
        db.session.commit()

        return {'id': spending.id}, 200