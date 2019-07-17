from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    email = db.Column(db.String(150), unique=True)
    sector = db.Column(db.String(150))
    password_hash = db.Column(db.String(128))
    super_admin = db.Column(db.Boolean)

    def __init__(self,
                 username,
                 email,
                 sector,
                 password_hash,
                 super_admin
                 ):
        self.username = username
        self.email = email
        self.sector = sector
        self.password_hash = password_hash
        self.super_admin = super_admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
