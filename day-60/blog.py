from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

app = Flask(__name__)

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/bce62c1197711b5ae23d")
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post")
def post_example():
    return render_template("post.html")


@app.route("/post/<int:num>")
def get_post(num):
    response = requests.get("https://api.npoint.io/bce62c1197711b5ae23d")
    all_posts = response.json()
    post_api = {}

    for post in all_posts:
        print(post["id"])
        if post["id"] == num:
            post_api = post

    return render_template("post_api.html", post=post_api)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        print(name, email, phone, message)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:User from Blog Post\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
            )
        return render_template("contact.html", message="Successfully sent message")
    else:
        return render_template("contact.html")


if __name__ == "__blog__":
    app.run()
