from flask import Flask, jsonify, render_template
from flask import request
from flask_wtf import Form
from wtforms import StringField,ValidationError, SelectField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
import os



app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'LutherCollege'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jkrbnkekcosnxb:jOrPwurv94mnMu7acVpIX0W2sA@ec2-54-197-230-161.compute-1.amazonaws.com:5432/da79ahfav90021'

db = SQLAlchemy(app)
Bootstrap(app)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'cs330ecomsite@gmail.com',
	MAIL_PASSWORD = os.environ.get('mail_pass')
	)


mail = Mail(app)

class Item(db.Model):
    __tablename__ = "Item"
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(6))
    size_w = db.Column(db.Integer)
    size_h = db.Column(db.Integer)

    def __init__(self,name,price,size_w,size_h):
        self.name = name
        self.price = price
        self.size_w = size_w
        self.size_h = size_h


class Contact(db.Model):
    __tablename__ = "Contact"
    item_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.String(1000))
    phone = db.Column(db.String(10))

    def __init__(self,name,email,message,phone):
        self.name = name
        self.email = email
        self.message = message
        self.phone = phone


class CommentsForm(Form):
    name = StringField('Name', validators=[InputRequired()])
    phone = StringField('Phone', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    comments = TextAreaField('Comments')


class PurchaseForm(Form):
    name = StringField('Name', validators=[InputRequired()])
    phone = StringField('Phone', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])




@app.route('/',methods=['GET','POST'])
def index():

    commentsform = CommentsForm() #commentsform at bottom of index page
    if commentsform.validate_on_submit():

        #store results in database
        name = commentsform.name.data
        phone = commentsform.phone.data
        email = commentsform.email.data
        comments = commentsform.comments.data

        newContact = Contact(name,email,comments,phone)
        db.session.add(newContact)
        db.session.commit()

        return render_template('index.html',commentsform=commentsform)

    return render_template('index.html',commentsform=commentsform)




@app.route('/discover',methods=['GET','POST'])
def discover():
    return render_template('discover.html')



@app.route('/buy',methods=['GET','POST'])
def buy():
    purchaseform = PurchaseForm()
    item = int(request.form['item'])
    res = Item.query.all()
    for k in res:
        if item == k.item_id:
            name = k.name
            price = k.price
    return render_template('buy.html', purchaseform = purchaseform, name = name)



@app.route('/checkout', methods=['GET','POST'])
def checkout():
    purchaseform = PurchaseForm()

    if purchaseform.validate_on_submit():
        #do mail stuff

        name = purchaseform.name.data
        phone = purchaseform.phone.data
        email = purchaseform.email.data
        address = purchaseform.address.data

        msg = Message(
            'Thanks for ordering!',
            sender='cs330ecomsite@gmail.com',
            recipients=
            [email])
    msg.body = "Hello " + name + "\n" + "Thank you for ordering from us. We're sending it! \n We will send it to " + address + "\n Thank you for your business!"
    mail.send(msg)

    return render_template('thanks.html', name = name)


'''
#We can easily add a purchasing extension by using Flask and Stripe.
#Here, we would use the form to gather the information and pass that into the charge method.
#Stripe would handle the financials, once we had a verified account and bank account set up.
#This is just an example.
@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    email = purchaseform.email.data

    customer = stripe.Customer.create(
        email=email,
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)
    #we would provide an html page with the charge information.
'''


if __name__ == "__main__":
    app.run()

