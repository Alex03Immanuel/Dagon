from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/sign-up', methods = ['POST','GET'])
def sign_up():

    enter_pswd = request.form.get('password1')
    reenter_pswd = request.form.get('password2')

    if enter_pswd != reenter_pswd:
        flash("The two passwords must match", category = "error")
    else:
        flash("Account created", category = "success")

    if request.method == "POST":
        data = request.form
        print(data)

    return render_template("sign-up.html")

@auth.route('/login')
def login():
    return "LOGIN"

@auth.route('/logout')
def logout():
    return "LOGOUT"



