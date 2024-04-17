from flask import Flask, request
app = Flask(__name__)
app.app_context().push()
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []

    for book in books:
        book_data = {'name': book.name, 'description': book.description}

        output.append(book_data)
    return {'books': output}


@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ({"name": book.name, "description": book.description})

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'], description=request.json['description'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return{"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet"}

if __name__ == '__main__':
    app.run(host='0.0.0.0')