from flask import Flask

from models import db, Man, Client
from routes import api

app = Flask(__name__)
app.register_blueprint(api)
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.add(Man(name='Bob'))
    db.session.add(Man(name='Rocky'))
    db.session.add(Client(name='Client 1', clientType='New', phone='2292929'))
    db.session.commit()

if __name__ == '__main__':
    app.run()
