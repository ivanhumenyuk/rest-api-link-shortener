from .models import Link, db
from apscheduler.schedulers.background import BackgroundScheduler
from app import app
import atexit
from sqlalchemy import func


def delete_inactive_link():
    with app.app_context():
        delete_query = Link.__table__.delete()\
            .where(Link.hash_lifetime == func.datediff(func.now(), Link.generated_day))
        db.session.execute(delete_query)
        db.session.commit()
        print('scheduler works')


scheduler = BackgroundScheduler()
scheduler.add_job(func=delete_inactive_link, trigger="interval", days=1)

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
