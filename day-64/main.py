from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy import Integer, VARCHAR, Float
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

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
    rating: Mapped[VARCHAR] = mapped_column(Float, nullable=False)
    ranking: Mapped[VARCHAR] = mapped_column(Integer, nullable=False)
    review: Mapped[VARCHAR] = mapped_column(VARCHAR(250), nullable=False)
    image_url: Mapped[VARCHAR] = mapped_column(VARCHAR(250), nullable=False)


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
    #         ranking=10,
    #         review="My favourite character was the caller.",
    #         image_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
    #     )
    #     new_movie2 = Movie(
    #         title="Avatar The Way of Water",
    #         year=2022,
    #         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #         rating=7.3,
    #         ranking=9,
    #         review="I liked the water.",
    #         image_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
    #     )
    #     db.session.add_all([new_movie1, new_movie2])
    #     db.session.commit()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
