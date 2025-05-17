from flask import Flask, render_template, request, session
from parte_2.classes.Book import Book
filename = "parte_2/data/"
from datafile import filename
from parte_2.classes.Member import Member
from parte_2.classes.Publisher import Publisher
from parte_2.classes.Requisition import Requisition
from parte_2.classes.userlogin import UserLogin
from parte_2.subs.apps_book import apps_book
from parte_2.subs.apps_gform import apps_gform 
from parte_2.subs.apps_subform import apps_subform 
from parte_2.subs.apps_userlogin import apps_userlogin

app = Flask(__name__)

Book.read("parte_2/data/library.db")
Member.read("parte_2/data/library.db")
Publisher.read("parte_2/data/library.db")
Requisition.read("parte_2/data/library.db")
UserLogin.read("parte_2/data/library.db")

app.secret_key = 'BAD_SECRET_KEY'
@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")
@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = UserLogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)
@app.route("/book", methods=["post","get"])
def book():
    return apps_book()
@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname):
    return apps_subform(cname)
@app.route("/UserLogin", methods=["post","get"])
def userlogin():
    return apps_userlogin()
if __name__ == '__main__':
    app.run()
    
    