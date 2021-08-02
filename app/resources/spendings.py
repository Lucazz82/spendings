from flask import request, jsonify, Response, make_response
from flask_restful import Resource
from database.models import db, Spending
from flask_jwt_extended import jwt_required, get_jwt_identity

class SpendingApi(Resource):
    @jwt_required()
    def get(self, user_id, spending_id):
        token_id = get_jwt_identity()
        if user_id != token_id: 
            return make_response({'msg': 'invalid credentials'}, 401)

        spending = Spending.query.filter_by(id = spending_id, user_id=user_id).first()

        return make_response(jsonify(spending.to_json()), 200)

    # Update spending
    @jwt_required()
    def put(self, user_id, spending_id):
        body = request.get_json()

        token_id = get_jwt_identity()
        if user_id != token_id: 
            return make_response({'msg': 'invalid credentials'}, 401)

        spending = Spending.query.filter_by(id=spending_id, user_id=user_id).first()

        spending.update(body)

        db.session.add(spending)
        db.session.commit()

        return 'success', 204


    # Delete spending
    @jwt_required()
    def delete(self, user_id, spending_id):
        token_id = get_jwt_identity()
        if user_id != token_id: 
            return make_response({'msg': 'invalid credentials'}, 401)
            
        spending = Spending.query.filter_by(id=spending_id, user_id=user_id).first()

        db.session.delete(spending)
        db.session.commit()

        return 'success', 204


class SpendingsApi(Resource):
    # Retrive all spendings from user
    @jwt_required()
    def get(self, user_id):
        token_id = get_jwt_identity()

        if user_id != token_id: 
            return make_response({'msg': 'invalid credentials'}, 401)

        spendings = Spending.query.filter_by(user_id=user_id)
        response = []

        for spending in spendings:
            response.append(spending.to_json())

        return make_response(jsonify(response), 200)
    
    # Add spending
    @jwt_required()
    def post(self, user_id):
        body = request.get_json()
        token_id = get_jwt_identity()

        if user_id != token_id: 
            return make_response({'msg': 'invalid credentials'}, 401)

        spending = Spending(**body)
        spending.user_id = user_id

        db.session.add(spending)
        db.session.commit()

        return {'id': spending.id}, 200