from flask import Blueprint

api = Blueprint('api',__name__)


@api.route('/')
def hello():
    return 'Hello, world!'
