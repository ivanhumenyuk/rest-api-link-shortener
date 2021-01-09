from db import db


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entered_link = db.Column(db.String(2048))
    generated_hash = db.Column(db.String(50))