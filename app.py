from flask import Flask, flash, render_template, request

app = Flask("HackathonApp")

@app.route('/')
def serveIndex():
    return render_template("layout.html")