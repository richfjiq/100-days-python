from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()


@app.route("/")
def home():
    return render_template("index.html", posts=post.posts)


@app.route("/post/<int:id>")
def show_post(id):
    requested_post = None
    for blog_post in post.posts:
        if blog_post['id'] == id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
