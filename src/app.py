from flask import Flask
from database import insert
from database.__init__ import initDatabase


app = Flask(__name__)

initDatabase()

if __name__ == "__main__":
    app.run(debug=True)