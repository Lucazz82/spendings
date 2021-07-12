from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# Database Models
class Spending(db.Model):
    __tablename__ = 'spendings'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String)
    instalments = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), nullable=False) # Datetime from JS
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'instalments': self.instalments,
            'date': self.date
        }


class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, unique= True, nullable=False)
    hash = db.Column(db.String, nullable=False)
    spendings = db.relationship('Spending', backref='user', lazy=True)



# API Routes
@app.route('/users', methods=['POST'])
def createUser():
    return


@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    return


@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    return


@app.route('/users/<id>', methods=['DELETE']) # Only admins
def deleteUser(id):
    return


@app.route('/users/<userId>/spendings', methods=['GET']) 
def getSpendings(userId):
    return


@app.route('/users/<userId>/spendings', methods=['POST']) 
def addSpending(userId):
    return


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