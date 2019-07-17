from app import db


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date_attendence = db.Column(db.DateTime)
    end_date_attendence = db.Column(db.DateTime)
    specific_start_date_attendence = db.Column(db.DateTime)
    specific_end_date_attendence = db.Column(db.DateTime)