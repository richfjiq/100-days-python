from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

"""
Make sure the required packages are installed:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
"""

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class BlogPostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired()])
    body = CKEditorField("Blog Content")
    submit = SubmitField("Create")


class UpdatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired()])
    body = CKEditorField("Blog Content")
    submit = SubmitField("Create")


@app.route("/")
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = (
        db.session.execute(db.select(BlogPost).order_by(BlogPost.date)).scalars().all()
    )
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route("/post/<int:post_id>")
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        with app.app_context():
            blog = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                author=form.author.data,
                img_url=form.img_url.data,
                body=form.body.data,
                date=date.today().strftime("%B %d, %Y"),
            )
            db.session.add(blog)
            db.session.commit()

            return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    post_to_update = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == id)
    ).scalar()
    # post_to_update = db.get_or_404(BlogPost, id)
    edit_form = UpdatePostForm(
        title=post_to_update.title,
        subtitle=post_to_update.subtitle,
        img_url=post_to_update.img_url,
        author=post_to_update.author,
        body=post_to_update.body,
    )

    if edit_form.validate_on_submit():
        post_to_update.title = edit_form.title.data
        post_to_update.subtitle = edit_form.subtitle.data
        post_to_update.author = edit_form.author.data
        post_to_update.img_url = edit_form.img_url.data
        post_to_update.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_to_update.id))

    return render_template("make-post.html", form=edit_form, edit=True)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete")
def delete():
    post_id = request.args.get("post_id")
    print(post_id)
    try:
        post_to_delete = db.get_or_404(BlogPost, post_id)
    except:
        return (
            jsonify(
                error=(
                    {
                        "Not Found": "Sorry a post with that id was not found in the database."
                    }
                )
            ),
            404,
        )
        return redirect(url_for("get_all_posts"))
    else:
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
