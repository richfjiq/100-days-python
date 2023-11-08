from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
    return render_template("login.html", email=email, password=password)


if __name__ == "__main__":
    app.run()
