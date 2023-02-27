from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    pin = db.Column(db.Integer)

    def __init__(self, user_name, password, pin):
        self.user_name = user_name
        self.password = password
        self.pin = pin


class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    car_name = db.Column(db.String(200))

    def __init__(self, car_name):
        self.car_name = car_name


class Bus(db.Model):
    __tablename__ = 'bus'
    id = db.Column(db.Integer, primary_key=True)
    bus_name = db.Column(db.String(200))

    def __init__(self, bus_name):
        self.bus_name = bus_name


class rickshaw(db.Model):
    __tablename__ = 'rickshaw'
    id = db.Column(db.Integer, primary_key=True)
    rickshaw_name = db.Column(db.String(200))

    def __init__(self, rickshaw_name):
        self.rickshaw_name = rickshaw_name


class cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    cart_name = db.Column(db.String(200))
    cart_wheels = db.Column(db.Integer)

    def __init__(self, cart_name, cart_wheels):
        self.cart_name = cart_name
        self.cart_wheels = cart_wheels


class boat(db.Model):
    __tablename__ = 'boat'
    id = db.Column(db.Integer, primary_key=True)
    boat_name = db.Column(db.String(200))

    def __init__(self, boat_name):
        self.boat_name = boat_name
