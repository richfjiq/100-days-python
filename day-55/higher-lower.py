from flask import Flask

app = Flask(__name__)
NUMBER_TO_GUESS = 7


@app.route("/")
def welcome():
    return '<h1>Guess a number between 0 and 9</h1>\
            <img src="https://media2.giphy.com/media/eikX1hbwlRkAQR8LAk/giphy.gif?cid=ecf05e474gky1gb5bwiafq69tpa6dnvt1yyrduh5z656dl8q&ep=v1_gifs_search&rid=giphy.gif&ct=g"/>'


@app.route("/<int:number>")
def guess_number(number):
    if number < NUMBER_TO_GUESS:
        return '<h1 style="color:red">Too low, try again!</h1>\
                <img src="https://media4.giphy.com/media/mLBNwdMcK83ClrlAJD/giphy.gif?cid=ecf05e47netumh4opdyjipyemx3vrdfypwifaf4rpz0ucesv&ep=v1_gifs_search&rid=giphy.gif&ct=g" />'
    elif number > NUMBER_TO_GUESS:
        return '<h1 style="color:blue">Too high, try again!</h1>\
                <img src="https://media2.giphy.com/media/oQAMOGT36CXk3BMOSr/giphy.gif?cid=ecf05e47mw3yv9cwiy9nhv0azzjalk4t8c08o0d26dgjne8q&ep=v1_gifs_search&rid=giphy.gif&ct=g" />'
    else:
        return '<h1 style="color:green">You find me 🎉</h1>\
                <img src="https://media4.giphy.com/media/jJQC2puVZpTMO4vUs0/giphy.gif?cid=ecf05e47zjmm8vneembkukgntd3ja52vf83tsan2jbko1v5u&ep=v1_gifs_search&rid=giphy.gif&ct=g" />'


if __name__ == "__main__":
    app.run()
