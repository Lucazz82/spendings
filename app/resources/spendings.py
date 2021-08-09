from database.models import Spending, db
from flask import Response, jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from werkzeug.exceptions import HTTPException, NotFound

from .errors import InvalidCredentials, MissingRequiredArgument, ServerError


class SpendingApi(Resource):
    @jwt_required()
    def get(self, user_id, spending_id):
        try:
            token_id = get_jwt_identity()

            if user_id != token_id: 
                raise InvalidCredentials

            spending = Spending.query.filter_by(id = spending_id, user_id=user_id).one_or_none()

            if spending is None:
                raise NotFound

            return make_response(jsonify(spending.to_json()), 200)

        except HTTPException as e:
            raise e
        except:
            raise ServerError

    # Update spending
    @jwt_required()
    def put(self, user_id, spending_id):
        try:
            body = request.get_json()

            token_id = get_jwt_identity()
            
            if user_id != token_id: 
                raise InvalidCredentials

            spending = Spending.query.filter_by(id=spending_id, user_id=user_id).one_or_none()

            if spending is None:
                raise NotFound

            spending.update(body)

            db.session.add(spending)
            db.session.commit()

            return 'success', 204

        except HTTPException as e:
            raise e
        except:
            raise ServerError


    # Delete spending
    @jwt_required()
    def delete(self, user_id, spending_id):
        try:
            token_id = get_jwt_identity()
            
            if user_id != token_id: 
                raise InvalidCredentials

            spending = Spending.query.filter_by(id=spending_id, user_id=user_id).one_or_none()

            if spending is None:
                raise NotFound

            db.session.delete(spending)
            db.session.commit()

            return 'success', 204

        except HTTPException as e:
            raise e
        except:
            raise ServerError


class SpendingsApi(Resource):
    # Retrive all spendings from user
    @jwt_required()
    def get(self, user_id):
        try:
            token_id = get_jwt_identity()

            if user_id != token_id: 
                raise InvalidCredentials

            spendings = Spending.query.filter_by(user_id=user_id)
            response = []

            for spending in spendings:
                response.append(spending.to_json())

            return make_response(jsonify(response), 200)

        except HTTPException as e: 
            raise e
        except:
            raise ServerError
    
    # Add spending
    @jwt_required()
    def post(self, user_id):
        try:
            body = request.get_json()
            token_id = get_jwt_identity()

            if user_id != token_id: 
                raise InvalidCredentials

            spending = Spending(**body)
            spending.user_id = user_id

            db.session.add(spending)
            db.session.commit()

            return {'id': spending.id}, 200

        except HTTPException as e:
            raise e
        except TypeError:
            raise MissingRequiredArgument
        except:
            raise ServerError
