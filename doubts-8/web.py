import requests
import bs4
from bs4 import BeautifulSoup as bs
from flask import Flask , render_template
app= Flask(__name__)

@app.route("/")
def step1():
    return render_template("index.html")

@app.route("/<name>")
def step(name):
    return (name)

if __name__ ==  "__main__":
    app.run(debug=True,port=8000)