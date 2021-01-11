from db import db
from utils import current_date


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entered_link = db.Column(db.String(2048))
    generated_hash = db.Column(db.String(50))
    generated_day = db.Column(db.Date(), default=current_date(), nullable=False)
    hash_lifetime = db.Column(db.Integer(), default=90, nullable=False)