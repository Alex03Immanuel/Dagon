from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return "<h1>Home Page</h1>"

@views.route('/sample')
def sample():
    return "<h1>sample</h1>"