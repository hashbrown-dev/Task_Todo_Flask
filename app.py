# from flask import Flask, render_template, request
#
# # from views.send_email import send_email
# from config.models import Feedback, db
#
# app = Flask(__name__)
#
# ENV = 'dev'
#
# if ENV == 'dev':
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/webtasks'
# else:
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mjrhmwafyhpsjc:d8a4604d6d8cd1d7544aa06831883708b67983cc9ed01de43067c6dc1d8eda88@ec2-52-22-135-159.compute-1.amazonaws.com:5432/d7ps0rj73nvblr'
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db.init_app(app)
# app.app_context().push()
#
#
# @app.before_first_request
# def create_tables():
#     print("printing before function fires")
#     db.create_all()
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         customer = request.form['customer']
#         dealer = request.form['dealer']
#         rating = request.form['rating']
#         comments = request.form['comments']
#         print(customer, dealer, rating, comments)
#         if customer == '' or dealer == '':
#             return render_template('index.html', message='Please enter required fields')
#         if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
#             data = Feedback(customer, dealer, rating, comments)
#             db.session.add(data)
#             db.session.commit()
#             # send_email(customer, dealer, rating, comments)
#             return render_template('dashboard.html')
#         return render_template('index.html', message='You have already submitted feedback')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config.blueprints import index_bp
# from send_mail import send_mail

app = Flask(__name__)

ENV = 'production'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/webtasks'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mjrhmwafyhpsjc:d8a4604d6d8cd1d7544aa06831883708b67983cc9ed01de43067c6dc1d8eda88@ec2-52-22-135-159.compute-1.amazonaws.com:5432/d7ps0rj73nvblr'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(index_bp)

db = SQLAlchemy(app)


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


@app.route('/')
def index():
    return render_template('/home/index')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            # send_mail(customer, dealer, rating, comments)
            # return render_template('./new_templates/dashboard.html')
            return render_template('new_templates/dashboard.html')
        return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
    app.run()
