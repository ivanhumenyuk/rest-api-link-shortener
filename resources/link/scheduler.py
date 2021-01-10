import atexit
from .models import Link, db
from utils import current_date
from apscheduler.schedulers.background import BackgroundScheduler
from app import app


def print_date_time():
    with app.app_context():
        timedelta = current_date() - Link.generated_day
        delete_query = Link.__table__.delete()\
            .where(timedelta >= Link.hash_lifetime)
        db.session.execute(delete_query)
        db.session.commit()
        print('scheduler works')
    # timedelta = current_date() - Link.generated_day


scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", days=1)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
