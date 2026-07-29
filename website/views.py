from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return "Home Page"

@views.route('/sample')
def sample():
    return "<h1>sample</h1>"