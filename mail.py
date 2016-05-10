from flask import Flask, request
from flask_mail import Mail, Message
import os

app =Flask(__name__)
mail=Mail(app)


app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'cs330ecomsite@gmail.com',
	MAIL_PASSWORD = os.environ.get('mail_pass')
	)

mail=Mail(app)

@app.route("/")
def index():

    address = request.args.get('address')
    name = request.args.get('name')


    msg = Message(
              'Thanks for ordering!',
           sender='cs330ecomsite@gmail.com',
           recipients=
               [address])
    msg.body = "Hello " + name + "\n" + "Thank you for ordering from us. We're sending it!"
    mail.send(msg)
    return "Sent"
if __name__ == "__main__":
    app.run()


