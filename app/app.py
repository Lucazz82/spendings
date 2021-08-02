from flask import Flask, jsonify, request
from database.models import db, User, Spending, initialize_database
from flask_restful import Api
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager
from resources.errors import errors

app = Flask(__name__)

# Configure database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/database.db' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/spendings'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_envvar('ENV_LOCATION')

api = Api(app, errors=errors)

jwt = JWTManager(app)

initialize_database(app)
initialize_routes(api)


if __name__ == '__main__':
    app.run()