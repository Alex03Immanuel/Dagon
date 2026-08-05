from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/sign-up', methods = ['POST','GET'])
def sign_up():

    enter_pswd = request.form.get('password1')
    reenter_pswd = request.form.get('password2')
    usernanme = request.form.get('username')  # check if username already exists later on 
    email = request.form.get('email') # check if user is already authenticated

    if enter_pswd != reenter_pswd:
        flash("The two passwords must match", category = "error")
    else:
        flash("Account created", category = "success")


    return render_template("sign-up.html")

@auth.route('/sign-in', methods = ['POST','GET'])
def login():
    
    # auth logic goes here 

    return render_template("sign-in.html")

@auth.route('/logout')
def logout():
    return "LOGOUT"



