from flask import Flask, render_template, request, session
from classes.Book import Book
filename = "data/"
from datafile import filename
from classes.Member import Member
from classes.Publisher import Publisher
from classes.Requisition import Requisition
from classes.userlogin import UserLogin
from subs.apps_book import apps_book
from subs.apps_gform import apps_gform 
from subs.apps_subform import apps_subform 
from subs.apps_userlogin import apps_userlogin

app = Flask(__name__)

Book.read("data/library.db")
Member.read("data/library.db")
Publisher.read("data/library.db")
Requisition.read("data/library.db")
UserLogin.read("data/library.db")

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
    print("Rotas registadas:")
    print(app.url_map)
    app.run()
    

    
    