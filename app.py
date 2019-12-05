from flask import Flask

from models import db, Man, Client
from routes import api, index

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.add(Man(name='Bob'))
    db.session.add(Man(name='Rocky'))
    db.session.add(Client(name='Client 1', clientType='New', phone='2292929'))
    db.session.add(Client(name='Client 2', clientType='Existing', phone='2282828'))
    db.session.add(Client(name='Client 3', clientType='Existing', phone='2757473'))
    db.session.commit()

if __name__ == '__main__':
    app.run()
