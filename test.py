from flask import Flask, jsonify, render_template
from flask import request
from flask_wtf import Form
from wtforms import StringField,ValidationError, SelectField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'LutherCollege'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jkrbnkekcosnxb:jOrPwurv94mnMu7acVpIX0W2sA@ec2-54-197-230-161.compute-1.amazonaws.com:5432/da79ahfav90021'

db = SQLAlchemy(app)
Bootstrap(app)




class CommentsForm(Form):
    name = StringField('Name', validators=[InputRequired()])
    phone = StringField('Phone', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    comments = TextAreaField('Comments')



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
    item = request.form['item']
    print("The item they want is '" + item + "'")
    return render_template('buy.html')


if __name__ == "__main__":
    app.run()

