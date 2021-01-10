from db import db
from utils import current_date


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entered_link = db.Column(db.String(2048))
    generated_hash = db.Column(db.String(50))
    generated_day = db.Column(db.Date(), default=current_date(), nullable=False)
    hash_lifetime = db.Column(db.Integer(), default=90, nullable=False)


def delete_inactive_event():
    # schedule_planner_var = 'SET GLOBAL event_scheduler = On;'
    delete_old_link_query = f"""CREATE EVENT IF NOT EXIST`delete_inactive` 
                            ON SCHEDULE 
                            EVERY 1 DAY DO DELETE FROM `link` 
                            WHERE SELECT DATEDIFF({current_date()}, `link.generated_day`) >= 
                            `link.generated_hash_lifetime`"""
    # db.engine.execute(schedule_planner_var)
    db.engine.execute(delete_old_link_query)