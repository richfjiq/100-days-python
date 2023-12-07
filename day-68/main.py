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

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key-goes-here"
Bootstrap5(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class RegisterForm(FlaskForm):
    name = StringField(
        "", validators=[DataRequired()], render_kw={"placeholder": "Name"}
    )
    email = StringField(
        "", validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"}
    )
    password = PasswordField(
        "", validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )
    submit = SubmitField("Sign me up")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/secrets")
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
def logout():
    pass


@app.route("/download")
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=8080)
