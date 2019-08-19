from app import db

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    description = db.Column(db.Text)

class SubArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    description = db.Column(db.Text)
    id_area = db.Column(db.Integer)
