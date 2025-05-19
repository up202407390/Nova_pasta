from flask import Flask, render_template, request, session
from classes.Book import Book

prev_option = ""

def apps_book():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Book.current()
            Book.remove(obj.id)
            if not Book.previous():
                Book.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Book.get_id(0))
            strobj = strobj + ';' + request.form["title"] + ';' + \
            request.form["author"] + ';' + request.form["genre"] + ';' + request.form["publisher_id"]
            obj = Book.from_string(strobj)
            Book.insert(obj.id)
            Book.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Book.current()
            obj.title = request.form["title"]
            obj.author = request.form["author"]
            obj.gender = request.form["genre"]
            obj.publisher_id = int(request.form["publisher_id"])
            Book.update(obj.id)
        elif option == "first":
            Book.first()
        elif option == "previous":
            Book.previous()
        elif option == "next":
            Book.nextrec()
        elif option == "last":
            Book.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Book.current()
        if option == 'insert' or len(Book.lst) == 0:
            id = 0
            id = Book.get_id(id)
            title = author = genre = publisher_id = ""
        else:
            id = obj.id
            title = obj.title
            author = obj.author
            genre = obj.genre
            publisher_id = obj.publisher_id
        return render_template("book.html", butshow=butshow, butedit=butedit,
                        id=id,title = title,author=author,genre=genre, publisher_id=publisher_id,
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

