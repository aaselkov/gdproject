from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Man(db.Model):
    __tablename__ = 'man'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {'id': self.id, 'name': self.name}


class Type(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {'id': self.id, 'name': self.name}


class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    clientTypeId = db.Column(db.Integer, ForeignKey('type.id'))
    clientType = relationship('Type')
    phone = db.Column(db.String(120))

    def json(self):
        return {'id': self.id, 'name': self.name, 'client type': self.clientType.json(), 'phone': self.phone}


class Treaty(db.Model):
    __tablename__ = 'treaty'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    clientId = db.Column(db.Integer, ForeignKey('client.id'))
    client = relationship('Client')

    def json(self):
        return {'id': self.id, 'name': self.name, 'client': self.client.json()}

