from flask import Flask, jsonify, render_template
from flask import request
from flask_wtf import Form
from wtforms import StringField,ValidationError, SelectField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'LutherCollege'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jkrbnkekcosnxb:jOrPwurv94mnMu7acVpIX0W2sA@ec2-54-197-230-161.compute-1.amazonaws.com:5432/da79ahfav90021'

db = SQLAlchemy(app)
Bootstrap(app)

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
    #need to make form for discover still

    commentsform = CommentsForm() #commentsform at bottom of index page
    if commentsform.validate_on_submit():

        #store results in database

        print(commentsform.name.data)
        print(commentsform.phone.data)
        print(commentsform.email.data)
        print(commentsform.comments.data)

        return render_template('index.html',commentsform=commentsform)

    return render_template('index.html',commentsform=commentsform)




@app.route('/discover',methods=['GET','POST'])
def discover():
    return render_template('discover.html')



@app.route('/buy',methods=['GET','POST'])
def buy():
    item = int(request.form['item'])
    res = Item.query.all()
    for k in res:
        if item == k.item_id:
            name = k.name
            price = k.price

    purchaseform = PurchaseForm()
    if purchaseform.validate_on_submit():
        #do mail stuff
        return render_template('thanks.html')



    return render_template('buy.html', purchaseform = purchaseform, name = name)




if __name__ == "__main__":
    app.run()

