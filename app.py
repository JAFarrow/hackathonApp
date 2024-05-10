from flask import Flask, flash, render_template, request

app = Flask("HackathonApp")
app.secret_key = "12345"

@app.route('/')
def serveIndex():
    # flash("Test")
    return render_template("cardCreation.html")