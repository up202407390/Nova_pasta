
from flask import Flask, render_template, request, session
from classes.userlogin import UserLogin

prev_option = ""

def apps_userlogin():
    print(">>> apps_userlogin foi chamada com sucesso!")

    global prev_option
    ulogin=session.get("user")
    user_id = UserLogin.get_user_id(ulogin)
    if (ulogin != None):
        print(">>> Utilizador autenticado:", ulogin)

        group = UserLogin.obj[user_id].usergroup
        if group != "admin":
            UserLogin.current(user_id)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = UserLogin.current()
            UserLogin.remove(obj.id)
            if not UserLogin.previous():
                UserLogin.first()
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            obj = UserLogin(0,request.form["user"],request.form["usergroup"], \
                            UserLogin.set_password(request.form["password"]))
            UserLogin.insert(obj.id)
            UserLogin.last()
        elif prev_option == 'edit' and option == 'save':
            obj = UserLogin.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = UserLogin.set_password(request.form["password"])
            UserLogin.update(obj.id)
        elif option == "first":
            UserLogin.first()
        elif option == "previous":
            UserLogin.previous()
        elif option == "next":
            UserLogin.nextrec()
        elif option == "last":
            UserLogin.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = UserLogin.current()
        if option == 'insert' or len(UserLogin.lst) == 0:
            user = ""
            usergroup = ""
            password = ""
        else:
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("userlogin.html", butshow=butshow, butedit=butedit, user=user,usergroup = usergroup,password=password, ulogin=session.get("user"), group=group)
    else:
        print(">>> Vai renderizar userlogin.html")

        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-
print("Função apps_userlogin carregada com sucesso!")


