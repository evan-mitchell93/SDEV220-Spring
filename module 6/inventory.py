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

@app.route('/inventory')
def inventory():
    items = Item.query.all()
    output = []
    for item in items:
        item_data = {'name':item.name,'expire':f"{item.expire.month}-{item.expire.day}-{item.expire.year}"}
        output.append(item_data)
    return {'items':output}


@app.route('/inventory',methods=["POST"])
def add_item():
    #get data from request
    item_name = request.json['name']
    item_date = datetime.strptime(request.json['date'],"%m-%d-%Y")
    #create new object
    new_item = Item(name=item_name,expire=item_date)

    #update database
    db.session.add(new_item)
    db.session.commit()
    return {"New item": new_item.name}

#remove all expired items and return the items that were removed
@app.route('/remove')
def remove_expired():
    output = []
    today = datetime.today()
    expired = Item.query.filter(Item.expire < today)
    for item in expired:
        item_data = {'name':item.name,'expire':f"{item.expire.month}-{item.expire.day}-{item.expire.year}"}
        output.append(item_data)
        db.session.delete(item)
    db.session.commit()
    return {"Removed items": output}

#Open csv and load data into the db
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

#update a specific item
@app.route('/<int:id>/update',methods=["POST"])
def update_item(id):
    item = Item.query.get(id)
    item.expire = datetime.strptime(request.json['date'],"%m-%d-%Y")
    db.session.commit()
    return {"Msg" : "Updated first item"}

if __name__ == "__main__":
    app.run(port=9999,debug=True)

