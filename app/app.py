from flask import Flask, jsonify, request
from databases.models import db, User, Spending, initialize_database
from flask_restful import Api
from resources.routes import initialize_routes


app = Flask(__name__)
api = Api(app)


# Configure database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/database.db' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/spendings'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

initialize_database(app)
initialize_routes(api)

# API Routes
# @app.route('/users', methods=['POST'])
# def createUser():
#     body = request.get_json()
#     # user = User(username=body['username'], hash=generate_password_hash(body['password']))
#     user = User(**body)
#     user.hash_password()

#     db.session.add(user)
#     db.session.commit()
#     return {'id': user.id}, 201


# @app.route('/users/<int:id>', methods=['GET']) # Check if it usefull because user doesn't have to much information to be usefull
# def getUser(id):
    # user = User.query.filter_by(id=id).first()
    # return user.to_json(), 200


@app.route('/users/<int:id>', methods=['PUT'])
def updateUser(id):
    body = request.get_json()
    
    user = User.query.filter_by(id=id).first()
    user.update(body)

    db.session.add(user)
    db.session.commit()
    return 'success', 204


@app.route('/users/<id>', methods=['DELETE']) # Only admins
def deleteUser(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    return 'success', 204


@app.route('/users/<userId>/spendings', methods=['GET']) 
def getSpendings(userId):
    spendings = Spending.query.filter_by(userId=userId)
    response = []

    for spending in spendings:
        response.append(spending.to_json())

    return jsonify(response), 200


@app.route('/users/<userId>/spendings', methods=['POST']) 
def addSpending(userId):
    body = request.get_json()
    spending = Spending(**body)
    spending.userId = userId

    db.session.add(spending)
    db.session.commit()

    return {'id': spending.id}, 200


@app.route('/users/<userId>/spendings/<spendingId>', methods=['GET']) 
def getSpending(userId, spendingId):
    return


@app.route('/users/<userId>/spendings/<spendingId>', methods=['PUT']) 
def updateSpending(userId, spendingId):
    return


@app.route('/users/<userId>/spendings/<spendingId>', methods=['DELETE']) 
def deleteSpending(userId, spendingId):
    return


@app.route('/login', methods=['POST'])
def login():
    return
