import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, logout_user
from flask_socketio import SocketIO, join_room, leave_room, send
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config.blueprints import index_bp
from config.models import db, Feedback, User, Bus, Car, rickshaw

# from send_mail import send_mail

app = Flask(__name__)

app.secret_key = 'secret'
app.config['WTF_CSRF_SECRET_KEY'] = "b'f\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/webtasks'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mjrhmwafyhpsjc:d8a4604d6d8cd1d7544aa06831883708b67983cc9ed01de43067c6dc1d8eda88@ec2-52-22-135-159.compute-1.amazonaws.com:5432/d7ps0rj73nvblr'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login = LoginManager(app)
login.init_app(app)

migrate = Migrate(app, db)
migrate.init_app(app, db)

app.register_blueprint(index_bp)


# db.init_app(app)
# app.app_context().push()
#
#
# @app.before_first_request
# def create_tables():
#     print("printing before function fires")
#     db.create_all()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login')
def login():
    context = {
        'userName': 'Harsh Gandhi',
    }
    return render_template('dashboard.html', context=context)


@app.route('/tasks')
def tasks():
    return render_template('tasks.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('base.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            # send_mail(customer, dealer, rating, comments)
            # return render_template('./new_templates/dashboard.html')
            return render_template('dashboard.html')
        return render_template('base.html', message='You have already submitted feedback')


if __name__ == '__main__':
    app.run()
