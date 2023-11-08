from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/bce62c1197711b5ae23d")
    all_posts = response.json()

    return render_template("index.html", posts=all_posts)


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


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
