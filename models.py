from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    table_id = db.Column(db.Integer)
    table_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    pwd = db.Column(db.String(255))
    is_active = db.Column(db.String(1))
    created = db.Column(db.Timestamp)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    full_name = db.Column(db.String(255))
    sex = db.Column(db.String(1))
    nik = db.Column(db.String(255), unique=True)
    created = db.Column(db.Timestamp)

class Presence(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    presence_date = db.Column(db.Timestamp)
    in_time = db.Column(db.Timestamp)
    out_time = db.Column(db.Timestamp, unique=True)
    staff_id = db.Column(db.Integer)