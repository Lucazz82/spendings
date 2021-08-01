from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class Spending(db.Model):
    __tablename__ = 'spendings'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(40), nullable=False)
    instalments = db.Column(db.Integer, nullable=False, default=1)
    date = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now()) # Datetime from JS. Change the default when JS will implemented
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


    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)


class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(40), unique= True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(102), nullable=False)
    spendings = db.relationship('Spending', backref='user', lazy=True)


    # Create exceptions for missing arguments
    def create_user(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.hash_password()



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


def initialize_database(app):
    db.init_app(app)
