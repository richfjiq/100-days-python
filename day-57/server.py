from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io/?name={name}")
    gender_response = requests.get(f"https://api.genderize.io/?name={name}")
    age = age_response.json()["age"]
    gender = gender_response.json()["gender"]
    return render_template("guess.html", name=name.capitalize(), age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/79033b02e537403ed53d")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run()
