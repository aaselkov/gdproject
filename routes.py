from flask import Blueprint, jsonify

from models import Man, db, Client

api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/people')
def get_people():
    return jsonify([(lambda man: man.json())(man) for man in Man.query.all()])


@api.route('/man/id/<int:man_id>')
def get_man(man_id):
    man = Man.query.get(man_id)
    return jsonify(man.json()) if man else ''


@api.route('/man/name/<int:man_id>,<string:man_name>')
def put_man(man_id, man_name):
    man = Man(id=man_id, name=man_name)
    db.session.add(man)
    db.session.commit()
    return 'done'


@api.route('/clients')
def get_clients():
    return jsonify([(lambda client: client.json())(client) for client in Client.query.all()])
