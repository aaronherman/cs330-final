from flask-sqlalchemy import SQLalchemy

app = Flask(__name__)
app.config[db url] = os.environ[database url]

db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = "Items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(6))
    size_w = db.Column(db.Integer(4))
    size_h = db.Column(db.Integer(4))

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

class History(db.Model):
    __tablename__ = "history"
    id = db.Column(db.Integer,primary_key=True)
    sold = db.Column(db.Integer(1000))
    available = db.Column(db.Integer(1000))

    def __init__(self,sold,available)
    self.sold = sold
    self.available = available

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
