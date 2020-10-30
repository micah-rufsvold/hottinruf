from flask import Flask, render_template, url_for, request, redirect, flash, make_resonse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fashy.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/base')
def base_test():
    return render_template('base.html')
@app.route('/game')
def game():
    return render_template('game.html')
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
   user = request.form['nm']
   room = request.form['gm']
   resp = make_response(render_template('game.html'))
   resp.set_cookie('userID', user)
   
   return resp


if __name__ == "__main__":
    app.run(debug=True)