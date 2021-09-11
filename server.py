from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def gqs_homepage():
    "Renders GQS homepage"
    return render_template('home.html')