from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from typing import Callable
from sqlalchemy import exc

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)

class MySQLAlchemy(SQLAlchemy):  # Or you can add the below code on the SQLAlchemy directly if you think to modify the package code is acceptable.
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable

db = MySQLAlchemy(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

if not os.path.isfile('sqlite:///movies.db'):
    db.create_all()



# After adding the new_movie the code needs to be commented out/deleted.
# So you are not trying to add the same movie twice.


try:
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )
    db.session.add(new_movie)
    db.session.commit()
except exc.IntegrityError:
    db.session.rollback()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
        try:
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data

        db.session.commit()

        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    try:
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get("https://api.themoviedb.org/3/search/movie/", params={"api_key": "907efd80a37845bfbc3924b7949bcba5", "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
    MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        #The language parameter is optional, if you were making the website for a different audience
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": "907efd80a37845bfbc3924b7949bcba5", "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        try:
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
        return redirect(url_for("rate_movie"))

if __name__ == '__main__':
    app.run(debug=True)