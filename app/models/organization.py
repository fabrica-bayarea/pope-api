from app import db


class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    tell = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    address = db.Column(db.String(150))
    city = db.Column(db.String(150))
    description = db.Column(db.Text)
    free = db.Column(db.Boolean)
    id_area = db.Column(db.Integer)
    id_sub_area = db.Column(db.Integer)
