from app import db


class Link(db.Model):
    link_id = db.Column(db.Integer, primery_key=True, auto_increment=True, unique=True)
    entered_link = db.Column(db.String(2048), unique=True)
    generated_short_link = db.Column(db.Dtring(50), unique=True)


