from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def landing_page():
    return "home .. sample .. sign-in .. logoff .. sign-up"

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/sample')
def sample():
    return "<h1>sample</h1>"