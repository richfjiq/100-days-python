import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, VARCHAR, Float
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# # cursor.execute(
# #     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# # )

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', 9.3)")

# db.commit()


# Initializing the extension
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# Configuring the extension
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[VARCHAR] = mapped_column(VARCHAR(250), unique=True, nullable=False)
    author: Mapped[VARCHAR] = mapped_column(VARCHAR(250), nullable=False)
    rating: Mapped[Float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"{self.title}"


with app.app_context():
    db.create_all()

with app.app_context():
    book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(book)
    db.session.commit()
