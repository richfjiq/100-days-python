from flask import Flask, jsonify, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from random import choice

"""
Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

API_KEY = "X.0}1Lw55QLhWyPJ?&{-"

app = Flask(__name__)

# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)

        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# http://127.0.0.1:5000/random
@app.route("/random")
def get_random():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = choice(cafes)
    # return jsonify(
    #     cafe={
    #         "id": random_cafe.id,
    #         "name": random_cafe.name,
    #         "map_url": random_cafe.map_url,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
    #         "has_sockets": random_cafe.has_sockets,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "seats": random_cafe.seats,
    #         "coffee_price": random_cafe.coffee_price,
    #     }
    # )
    return jsonify(cafe=random_cafe.to_dict())


# http://127.0.0.1:5000/all
@app.route("/all")
def gel_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# HTTP GET - Read Record
# http://127.0.0.1:5000/search?loc=South%20Kensington
@app.route("/search")
def find_a_cafe():
    location = request.args.get("loc")
    cafes_in_location = (
        db.session.execute(db.select(Cafe).where(Cafe.location == location))
        .scalars()
        .all()
    )
    if len(cafes_in_location) == 0:
        return jsonify(
            error={"Not Found": "Sorry, we don't have a cafe at the location."}
        )
    else:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes_in_location])


# HTTP POST - Create Record
# http://127.0.0.1:5000/add
@app.route("/add", methods=["POST"])
def add():
    # sending body - x-www-form-urlencoded in Postman
    # new_cafe = Cafe(
    #     name=request.form.get("name"),
    #     map_url=request.form.get("map_url"),
    #     img_url=request.form.get("img_url"),
    #     location=request.form.get("loc"),
    #     has_sockets=bool(request.form.get("sockets")),
    #     has_toilet=bool(request.form.get("toilet")),
    #     has_wifi=bool(request.form.get("wifi")),
    #     can_take_calls=bool(request.form.get("calls")),
    #     seats=request.form.get("seats"),
    #     coffee_price=request.form.get("coffee_price"),
    # )
    # db.session.add(new_cafe)
    # db.session.commit()

    # sending body - raw - JSON in Postman
    data = request.json
    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=data["has_toilet"],
        has_wifi=data["has_wifi"],
        has_sockets=data["has_sockets"],
        can_take_calls=data["can_take_calls"],
        coffee_price=data["coffee_price"],
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response=({"success": "Successfully added the new cafe."}))


# HTTP PUT/PATCH - Update Record
# http://127.0.0.1:5000/update-price/22?new_price=£2.80
@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):
    new_price = request.args.get("new_price")

    cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
    print(cafe_to_update)

    if cafe_to_update == None:
        return (
            jsonify(
                error=(
                    {
                        "Not Found": "Sorry a cafe with that id was not found in the database."
                    }
                )
            ),
            404,
        )
    else:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Successfully updated the price."})


# HTTP DELETE - Delete Record
# http://127.0.0.1:5000/report-closed/22?api-key=X.0}1Lw55QLhWyPJ?%26{-
@app.route("/report-closed/<int:id>", methods=["DELETE"])
def report_closed(id):
    api_key_param = request.args.get("api-key")
    if api_key_param == API_KEY:
        try:
            cafe_to_delete = db.get_or_404(Cafe, id)
        except:
            return (
                jsonify(
                    error=(
                        {
                            "Not Found": "Sorry a cafe with that id was not found in the database."
                        }
                    )
                ),
                404,
            )
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({"deleted": "Cafe has been deleted from database."})
    else:
        return (
            jsonify(
                {
                    "error": "Sorry, that's not allowed. Make sure you have the correct apy_key."
                }
            ),
            404,
        )


if __name__ == "__main__":
    app.run(debug=True)
