from flask import Flask, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

app.app_context().push()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    #expiration date
    expire = db.Column(db.DateTime())

    def __str__(self):
        return f"{self.name}"
    

@app.route('/')
def index():
    return 'hello'

@app.route('/load',methods=["GET"])
def load_csv():
    db.create_all()
    df = pd.read_csv('food.csv')
    for index,row in df.iterrows():
        dateObj = datetime.strptime(row['expiration date'],"%m-%d-%Y")
        item = Item(name=row['name'],expire=dateObj)
        db.session.add(item)
    db.session.commit()
    return "Done"

if __name__ == "__main__":
    app.run(port=9999,debug=True)

