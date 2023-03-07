from flask import Flask, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=open("secret.txt").read())
# db.init_app(app)


@app.route("/")
def landing():
    return render_template("index.html")