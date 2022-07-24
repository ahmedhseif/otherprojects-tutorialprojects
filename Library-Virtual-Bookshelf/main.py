from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
import os
from sqlalchemy import exc
# This is SQLite but check below it the SQLAlchemy
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books ("
#                "id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")
# cursor.execute("INSERT OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class MySQLAlchemy(SQLAlchemy):  # Or you can add the below code on the SQLAlchemy directly if you think to modify the package code is acceptable.
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable

db = MySQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


if not os.path.isfile('sqlite:///movies.db'):
    db.create_all()




@app.route('/')
def home():
    ##READ ALL RECORDS
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # new_book = {
        #     "title": request.form["title"],
        #     "author": request.form["author"],
        #     "rating": request.form["rating"]
        # }
        # all_books.append(new_book)
        new_book = Book(title=request.form["title"],
                        author=request.form["author"],
                        rating=request.form["rating"])
        try:
            db.session.add(new_book)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

        # NOTE: You can use the redirect method from flask to redirect to another route
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))

    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)