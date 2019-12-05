from flask import Flask

from models import db, Client, Type, Treaty
from routes import api, index

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    # db.session.add(Man(name='Bob'))
    # db.session.add(Man(name='Rocky'))
    existing = Type(name='Existing')
    new = Type(name='New')
    db.session.add(existing)
    db.session.add(new)
    db.session.commit()
    cli1 = Client(name='Client 1', clientTypeId=existing.id, phone='2292929')
    cli2 = Client(name='Client 2', clientTypeId=existing.id, phone='2282828')
    cli3 = Client(name='Client 3', clientTypeId=new.id, phone='2757473')
    db.session.add(cli1)
    db.session.add(cli2)
    db.session.add(cli3)
    db.session.commit()
    dog1 = Treaty(name='Dogovor 1', clientId=cli1.id)
    dog2 = Treaty(name='Dogovor 2', clientId=cli2.id)
    dog3 = Treaty(name='Dogovor 3', clientId=cli3.id)
    db.session.add(dog1)
    db.session.add(dog2)
    db.session.add(dog3)
    db.session.commit()

if __name__ == '__main__':
    app.run()
