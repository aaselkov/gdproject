from flask import Flask

from models import db, Client, Type
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
    db.session.add(Client(name='Client 1', clientTypeId=existing.id, phone='2292929'))
    db.session.add(Client(name='Client 2', clientTypeId=existing.id, phone='2282828'))
    db.session.add(Client(name='Client 3', clientTypeId=new.id, phone='2757473'))
    db.session.commit()

if __name__ == '__main__':
    app.run()
