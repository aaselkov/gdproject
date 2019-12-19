from flask import Blueprint, jsonify

from models import Man, db, Client, Treaty, Type

index = Blueprint('index',__name__, url_prefix='/')
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


@api.route('/treaty')
def get_treaty():
    return jsonify([(lambda treaty: treaty.json())(treaty) for treaty in Treaty.query.all()])


@api.route('/clients')
def get_clients():
    return jsonify([(lambda client: client.json())(client) for client in Client.query.all()])


@api.route('/clients/new/<int:cli_id>,<string:cli_name>,<int:cli_type>,<string:cli_phone>')
def new_client(cli_id, cli_name, cli_type, cli_phone):
    client = Client(id=cli_id, name=cli_name, clientTypeId=cli_type, phone=cli_phone)
    db.session.add(client)
    db.session.commit()
    return 'done'


@api.route('/type/new/<string:type_name>')
def new_type(type_name):
    typenew = Type(name=type_name)
    db.session.add(typenew)
    db.session.commit()
    return 'done'


@index.route('/')
@index.route('/index')
def get_index():
    return '''
            <html>
                <title>
                GD Project application web service
                </title>
                <body>
                    <h3>API:</h3>
                    <a href='./api/people'>People</a>
                </body>
            </html>
           '''
