from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy import Integer, VARCHAR, Float, asc, desc
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_TOKEN = os.getenv("TMDB_TOKEN")

headers = {"accept": "application/json", "Authorization": f"Bearer {TMDB_TOKEN}"}

"""
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
Bootstrap5(app)
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[VARCHAR] = mapped_column(VARCHAR(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[VARCHAR] = mapped_column(VARCHAR(350), nullable=False)
    rating: Mapped[Float] = mapped_column(Float, nullable=False)
    ranking: Mapped[VARCHAR] = mapped_column(VARCHAR(10), nullable=False)
    review: Mapped[VARCHAR] = mapped_column(VARCHAR(250), nullable=False)
    image_url: Mapped[VARCHAR] = mapped_column(VARCHAR(250), nullable=False)


class EditForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # create the database
    # with app.app_context():
    #     db.create_all()

    # adds two movies to the database
    # with app.app_context():
    #     new_movie1 = Movie(
    #         title="Phone Booth",
    #         year=2002,
    #         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #         rating=7.3,
    #         ranking="10",
    #         review="My favourite character was the caller.",
    #         image_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
    #     )
    #     new_movie2 = Movie(
    #         title="Avatar The Way of Water",
    #         year=2022,
    #         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #         rating=7.3,
    #         ranking="9",
    #         review="I liked the water.",
    #         image_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
    #     )
    #     db.session.add_all([new_movie1, new_movie2])
    #     db.session.commit()

    movies = db.session.execute(db.select(Movie).order_by(desc(Movie.rating))).scalars().all()

    for index in range(len(movies)):
        print(movies[index])
        movie_to_update = db.session.execute(
            db.select(Movie).where(Movie.id == movies[index].id)
        ).scalar()
        movie_to_update.ranking = f"{index + 1}"
        db.session.commit()

    return render_template("index.html", movies=movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    movie = db.get_or_404(Movie, id)

    if form.validate_on_submit():
        with app.app_context():
            movie_to_update = db.session.execute(
                db.select(Movie).where(Movie.id == id)
            ).scalar()
            movie_to_update.rating = form.rating.data
            movie_to_update.review = form.review.data
            db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        print(movie_title)
        response = requests.get(
            f"https://api.themoviedb.org/3/search/movie?query={movie_title}",
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()["results"]
        print(data)
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/find")
def find():
    movie_id = request.args.get("id")
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}", headers=headers
    )
    response.raise_for_status()
    data = response.json()

    with app.app_context():
        movie = Movie(
            title=data["title"],
            year=data["release_date"][0:4],
            description=data["overview"],
            rating=0,
            ranking="None",
            review="None",
            image_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}",
        )
        db.session.add(movie)
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
