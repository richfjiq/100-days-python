from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, VARCHAR, Float, update
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
Bootstrap5(app)
db.init_app(app)

all_books = []


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[VARCHAR] = mapped_column(VARCHAR(250), unique=True, nullable=False)
    author: Mapped[VARCHAR] = mapped_column(VARCHAR(250), nullable=False)
    rating: Mapped[Float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"self.title"


class BookForm(FlaskForm):
    name = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = SelectField(
        "Rating", choices=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    )
    submit = SubmitField("Submit")


class UpdateRatingForm(FlaskForm):
    new_rating = SelectField(
        "New Rating", choices=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    )
    submit = SubmitField("Submit")


@app.route("/")
def home():
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()

    return render_template("index.html", books=books)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()

    if form.validate_on_submit():
        with app.app_context():
            db.create_all()

        with app.app_context():
            book = Book(
                title=form.name.data,
                author=form.author.data,
                rating=int(form.rating.data),
            )
            db.session.add(book)
            db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/edit/<int:num>", methods=["GET", "POST"])
def edit(num):
    form = UpdateRatingForm()
    book = db.get_or_404(Book, num)

    if form.validate_on_submit():
        with app.app_context():
            book_to_update = db.session.execute(
                db.select(Book).where(Book.id == num)
            ).scalar()
            book_to_update.rating = form.new_rating.data
            db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", form=form, book=book)


if __name__ == "__main__":
    app.run(debug=True)
