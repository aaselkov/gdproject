from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Man(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {'id': self.id, 'name': self.name}


class Client(Man):
    __tablename__ = 'clients'
    clientType = db.Column(db.String(120))
    phone = db.Column(db.String(120))

    def json(self):
        return {'id': self.id, 'name': self.name,'client type': self.clientType, 'phone': self.phone}


class Treaty(db.Model):
    __tablename__ = 'treaty'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    client = db.Column(db.Integer)

    def json(self):
        return {'id': self.id, 'name': self.name,'date': self.date, 'client': self.client}

