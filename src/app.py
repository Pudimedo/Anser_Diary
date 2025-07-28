from flask import Flask, render_template
from database import insert
from werkzeug.security import check_password_hash, generate_password_hash
from database.__init__ import initDatabase
import sqlite3


app = Flask(__name__)

app.secret_key = "UDD36D)6+1&4.W5l3I33x^Qivr=gbT[t{r3u#aQ,+/GA<>10J!"

initDatabase()



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)