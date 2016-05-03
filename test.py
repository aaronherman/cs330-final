from flask import Flask, jsonify, render_template
from flask import request


app = Flask(__name__)
app.debug = True


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

