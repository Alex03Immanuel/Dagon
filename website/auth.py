from flask import Blueprint, render_template,request

auth = Blueprint('auth',__name__)

@auth.route('/sign-up', methods = ['POST','GET'])
def sign_up():
    return render_template("sign-up.html")

@auth.route('/login')
def login():
    return "LOGIN"

@auth.route('/logout')
def logout():
    return "LOGOUT"



