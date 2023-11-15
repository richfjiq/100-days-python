from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        label="Password",
        validators=[DataRequired(), Length(min=8)],
    )
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "ZeWHKvkoqhEiehMjW5kYeCiE4ecAdshPRje55K6u"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        print(email)
        print(password)
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
