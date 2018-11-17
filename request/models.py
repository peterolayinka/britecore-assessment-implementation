import enum
from datetime import datetime 

from . import db

class ProductEnum(enum.Enum):
    policies = 'Policies'
    billing = 'Billing'
    claims = 'Claims'
    report = 'Reports'

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    request = db.relationship('Request', backref='client', lazy='dynamic')

    def __repr__(self):
       return f"<Client(name='{self.name}')>"

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    priority = db.Column(db.Integer)
    target_date = db.Column(db.Date)
    product = db.Column(db.Enum(ProductEnum))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
       return f"<Request(client='{self.client}', title='{self.title}', priority='{self.priority}')>"