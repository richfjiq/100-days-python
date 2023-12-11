from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
Bootstrap5(app)

# Flask-Login -- Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy()
db.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=generate_password_hash(
                request.form.get("password"), method="pbkdf2", salt_length=8
            ),
        )
        try:
            db.session.add(user)
            db.session.commit()
        except:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))
        else:
            # Log in and authenticate user after adding details to database.
            login_user(user)

            return redirect(url_for("secrets"))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user == None:
            flash("This email does not exist, please try again.")
        else:
            print(user)
            # Check stored password hash against entered password hashed
            if check_password_hash(user.password, password):
                login_user(user)
                flash("You were successfully logged in")
                return redirect(url_for("secrets"))
            else:
                flash("Password incorrect, please try again.")

    return render_template("login.html", logged_in=current_user.is_authenticated)


# Only logged-in users can access the route
@app.route("/secrets")
@login_required
def secrets():
    print(current_user.name)
    # Passing the name from the current_user
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


# Only logged-in users can download the pdf
@app.route("/download")
@login_required
def download():
    return send_from_directory("static/files", "cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
