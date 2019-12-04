from flask import Blueprint, jsonify

from models import Men

api = Blueprint('api',__name__)


@api.route('/')
def hello():
    return jsonify([(lambda men: men.json())(men) for men in Men.query.all()])
