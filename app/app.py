from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)


# Configure database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/database.db' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/spendings'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# Database Models
class Spending(db.Model):
    __tablename__ = 'spendings'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(40))
    instalments = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), nullable=False) # Datetime from JS
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_json(self):
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
    username = db.Column(db.String(40), unique= True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(102), nullable=False)
    spendings = db.relationship('Spending', backref='user', lazy=True)


    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    
    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            
            if key == 'password':
                self.hash_password()


    def hash_password(self):
        self.password = generate_password_hash(self.password)


    def check_password(self, password):
        return check_password_hash(self.password, password)


db.create_all()



# API Routes
@app.route('/users', methods=['POST'])
def createUser():
    body = request.get_json()
    # user = User(username=body['username'], hash=generate_password_hash(body['password']))
    user = User(**body)
    user.hash_password()

    db.session.add(user)
    db.session.commit()
    return {'id': user.id}, 201


@app.route('/users/<id>', methods=['GET']) # Check if it usefull because user doesn't have to much information to be usefull
def getUser(id):
    user = User.query.filter_by(id=id).first()
    return user.to_json(), 200


@app.route('/users/<id>', methods=['PUT'])
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