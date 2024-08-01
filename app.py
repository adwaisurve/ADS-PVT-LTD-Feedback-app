from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
# from gunicorn.app.base import Application 
# from gunicorn import util 
# import fcntl 

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Adwai31@localhost:5432/lexus'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Adwai31@localhost:5432/lexus'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200))  # Added email field
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, email, dealer, rating, comments):  # Added email parameter
        self.customer = customer
        self.email = email  # Initialize email
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

# Drop and recreate the table
with app.app_context():
    # db.drop_all()  # Drop existing tables
    db.create_all()  # Create new tables with updated schema

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        email = request.form['email']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or dealer == '' or email == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, email, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, email, dealer, rating, comments)
            return render_template('success.html')
        else:
            return render_template('index.html', message='You have already submitted feedback')
    else:
        return render_template('index.html', message='Invalid request method')

if __name__ == '__main__':
    app.run()
##gunicorn port number is 8000