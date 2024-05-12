from flask import Flask, session, render_template, request, redirect
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "12345"
Session(app)

@app.route('/', methods=["GET"])
def serveIndex():
    return render_template("cardCreation.html", nav="deck")

@app.route('/deck', methods=["GET", "POST"])
def serveDeck():
    if request.method == "POST":
        addCardToStorage(request.form.get("question"), request.form.get("answer"))
        return redirect("/redirect")
    else:
        return render_template("deck.html", deck=retrieveCards(), nav="home")
    
@app.route("/redirect", methods=["GET"])
#This is a hacky way to prevent form resubmission on page reload, not recommended for anything serious :3
def redirectCheese():
    return redirect("/deck")

@app.route("/clear", methods=["Get"])
def clearSession():
    session.clear()
    return redirect("/deck")
    
def addCardToStorage(front, back):
    try:
        test = session["deck"]
    except KeyError:
        session["deck"] = []
    session["deck"].append({"front": front, "back": back})


def retrieveCards():
    try:
        test = session["deck"]
    except KeyError:
        session["deck"] = []
    return session["deck"]