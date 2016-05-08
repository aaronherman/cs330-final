from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jkrbnkekcosnxb:jOrPwurv94mnMu7acVpIX0W2sA@ec2-54-197-230-161.compute-1.amazonaws.com:5432/da79ahfav90021'

db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = "Items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(6))
    size_w = db.Column(db.Integer)
    size_h = db.Column(db.Integer)

    def __init__(self,name,price,size_w,size_h):
        self.name = name
        self.price = price
        self.size_w = size_w
        self.size_h = size_h

class Description(db.Model):
    __tablename__ = "description"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    img = db.Column(db.String(250))
    blue = db.Column(db.Boolean())
    red = db.Column(db.Boolean())
    orange = db.Column(db.Boolean())
    yellow = db.Column(db.Boolean())
    purple = db.Column(db.Boolean())
    green = db.Column(db.Boolean())


    def __init__(self,description,img):
        self.description = description
        self.img = img

    #Description(id= , description = , img = , blue = , red = , orange = , yellow =, purple = , green =)

class History(db.Model):
    __tablename__ = "history"
    id = db.Column(db.Integer,primary_key=True)
    sold = db.Column(db.Integer)
    available = db.Column(db.Integer)

    def __init__(self,sold,available):
        self.sold = sold
        self.available = available

    #History(id=,sold=,available=)

class Contact(db.Model):
    __tablename__ = "contact"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.String(1000))
    phone = db.Column(db.String(10))

    def __init__(self,name,email,message,phone):
        self.name = name
        self.email = email
        self.message = message
        self.phone = phone


db.create_all()


'''
Item(id = 1,name = 'circle canvas',price = 175,size_w = 24,size_h=24)
Description(id=1, description = 'circular canvas, with deer and red.', img = 'ht_1.jpg', blue = False, red = True, orange = True, yellow = True, purple = False, green = False)
History(id=1,sold=0,available=1)

Item(id = 2,name = 'square canvas',price = 150,size_w = 24,size_h=24)
Description(id=2, description = 'square canvas with human and abstract art', img = 'ht_2.jpg', blue = True, red = True, orange = True, yellow =False, purple = False, green =True)
History(id=2,sold=0,available=1)


Item(id = 3,name = 'square canvas',price = 150,size_w = 24,size_h=24)
Description(id=3, description = 'square canvas with abstract painting', img = 'ht_3.jpg', blue = False, red = True, orange = True, yellow =True, purple = False, green =True)
History(id=3,sold=0,available=1)

Item(id = 4,name = 'circle canvas',price = 175,size_w = 24,size_h=24)
Description(id=4, description = 'circular canvas with ', img = 'ht_4.jpg', blue = True, red = True, orange =True, yellow =True, purple = False, green =False)
History(id=4,sold=0,available=1)


Item(id = 5,name = 'square canvas',price = 180,size_w = 24,size_h=24)
Description(id=5, description = 'abstract square canvas with blue trees, lines', img = 'ht_5.jpg', blue =True, red =True, orange =True, yellow =True, purple =False, green =True)
History(id=5,sold=0,available=1)

Item(id = 6,name = 'square canvas',price = 150,size_w = 24,size_h=24)
Description(id=6, description ='square canvas with valley and pine trees', img = 'ht_6.jpg', blue = True, red =False, orange =True, yellow =True, purple =False, green =False)
History(id=6,sold=0,available=1)

Item(id = 7,name = 'rectangle drawing',price = 10,size_w = 4,size_h=6)
Description(id=7, description = 'tree drawing', img = 'ht_7.jpg', blue = False, red = False, orange = False, yellow =False, purple = False, green =True)
History(id=7,sold=0,available=1)

Item(id = 8,name = 'square drawing',price = 10,size_w = 5,size_h=5)
Description(id=8, description = 'tree drawing', img = 'ht_8.jpg', blue = False, red = False, orange = False, yellow =False, purple = False, green =True)
History(id=8,sold=0,available=1)

Item(id = 9,name = 'square drawing',price = 10,size_w = 5,size_h=5)
Description(id=9, description = 'tree drawing', img = 'ht_9.jpg', blue = False, red = False, orange = False, yellow =False, purple = False, green =True)
History(id=9,sold=0,available=1)

'''