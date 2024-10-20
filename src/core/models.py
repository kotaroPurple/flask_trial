
from core.app import (app, db)


class Customer(db.Model):
    __tablename__ = 'customers'

    customer_id = db.Column(db.String, primary_key=True)
    customer_name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.Boolean)

    purchases = db.relationship('Purchase', backref='customers', cascade='delete')


class Purchase(db.Model):
    __tablename__ = 'purchases'

    purchase_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.String, db.ForeignKey("customers.customer_id"))
    date = db.Column(db.DateTime)


class Item(db.Model):
    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer)


with app.app_context():
    db.create_all()
