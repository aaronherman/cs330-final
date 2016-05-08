from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jkrbnkekcosnxb:jOrPwurv94mnMu7acVpIX0W2sA@ec2-54-197-230-161.compute-1.amazonaws.com:5432/da79ahfav90021'

db = SQLAlchemy(app)

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

    #Item(item_id=,name=,price=,size_w=,size_h)

class Description(db.Model):
    __tablename__ = "Description"
    item_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    img = db.Column(db.String(250))
    blue = db.Column(db.Boolean,default=False,nullable=False)
    red = db.Column(db.Boolean,default=False,nullable=False)
    orange = db.Column(db.Boolean,default=False,nullable=False)
    yellow = db.Column(db.Boolean,default=False,nullable=False)
    purple = db.Column(db.Boolean,default=False,nullable=False)
    green = db.Column(db.Boolean,default=False,nullable=False)


    def __init__(self,description,img,blue,red,orange,yellow,purple,green):
        self.description = description
        self.img = img
        self.blue = blue
        self.red = red
        self.orange = orange
        self.yellow = yellow
        self.purple = purple
        self.green = green

    #Description(item_id= , description = , img = , blue = , red = , orange = , yellow =, purple = , green =)

class History(db.Model):
    __tablename__ = "History"
    item_id = db.Column(db.Integer,primary_key=True)
    sold = db.Column(db.Integer)
    available = db.Column(db.Integer)

    def __init__(self,sold,available):
        self.sold = sold
        self.available = available

    #History(item_id=,sold=,available=)

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


#db.create_all()

'''
item1 = Item(name = 'circle canvas',price = 175,size_w = 24,size_h=24)
descrip1 = Description(description = 'circular canvas, with deer and red.', img = 'ht_1.jpg', blue = False, red = True, orange = True, yellow = True, purple = False, green = False)
history1 = History(sold=0,available=1)

item2 = Item(name = 'square canvas',price = 150,size_w = 24,size_h=24)
descrip2 = Description(description = 'square canvas with human and abstract art', img = 'ht_2.jpg', blue = True, red = True, orange = True, yellow =False, purple = False, green =True)
history2 = History(sold=0,available=1)


item3 = Item(name = 'square canvas',price = 150,size_w = 24,size_h=24)
descrip3 = Description( description = 'square canvas with abstract painting', img = 'ht_3.jpg', blue = False, red = True, orange = True, yellow =True, purple = False, green =True)
history3 = History(sold=0,available=1)

item4 = Item(name = 'circle canvas',price = 175,size_w = 24,size_h=24)
descrip4 = Description(description = 'circular canvas with ', img = 'ht_4.jpg', blue = True, red = True, orange =True, yellow =True, purple = False, green =False)
history4 = History(sold=0,available=1)


item5 = Item(name = 'square canvas',price = 180,size_w = 24,size_h=24)
descrip5 = Description(description = 'abstract square canvas with blue trees, lines', img = 'ht_5.jpg', blue =True, red =True, orange =True, yellow =True, purple =False, green =True)
history5 = History(sold=0,available=1)

item6 = Item(name = 'square canvas',price = 150,size_w = 24,size_h=24)
descrip6 = Description(description ='square canvas with valley and pine trees', img = 'ht_6.jpg', blue = True, red =False, orange =True, yellow =True, purple =False, green =False)
history6 = History(sold=0,available=1)

item7 = Item(name = 'rectangle drawing',price = 10,size_w = 4,size_h=6)
descrip7 = Description(description = 'tree drawing', img = 'ht_7.jpg', blue = False, red = False, orange = False, yellow =False, purple = False, green =True)
history7 = History(sold=0,available=1)

item8 = Item(name = 'square drawing',price = 10,size_w = 5,size_h=5)
descrip8 = Description( description = 'tree drawing', img = 'ht_8.jpg', blue = False, red = False, orange = False, yellow =False, purple = False, green =True)
history8 = History(sold=0,available=1)

item9 = Item(name = 'square drawing',price = 10,size_w = 5,size_h=5)
descrip9 = Description(description = 'tree drawing', img = 'ht_9.jpg', blue = False, red = False, orange = False, yellow =False, purple = False, green =True)
history9 = History(sold=0,available=1)

db.session.add(item1)
db.session.add(descrip1)
db.session.add(history1)
db.session.add(item2)
db.session.add(descrip2)
db.session.add(history2)
db.session.add(item3)
db.session.add(descrip3)
db.session.add(history3)
db.session.add(item4)
db.session.add(descrip4)
db.session.add(history4)
db.session.add(item5)
db.session.add(descrip5)
db.session.add(history5)
db.session.add(item6)
db.session.add(descrip6)
db.session.add(history6)
db.session.add(item7)
db.session.add(descrip7)
db.session.add(history7)
db.session.add(item8)
db.session.add(descrip8)
db.session.add(history8)
db.session.add(item9)
db.session.add(descrip9)
db.session.add(history9)
db.session.commit()
'''

qu = Item.query.all()
for item in qu:
    print(item.price)


'''
num_deleted = db.session.query(Item).delete()
db.session.commit()
print(num_deleted)

qu = Item.query.all()
for item in qu:
    print(item.price)
'''