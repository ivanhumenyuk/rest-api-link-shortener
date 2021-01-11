from .models import Link, db
from utils import hash_prettier


def destroy_collision(hash_string: str, x=0, y=7) -> str:
    """
    Function that destroy destroy hash collision and repeating in database.
    :param hash_string: long hash string of entered link
    :param x: start of string slice
    :type x: int
    :param y:stop of string slice
    :type y:int
    """
    short_hash = hash_string[x: y]
    pretty_hash_string = hash_prettier(short_hash)
    db_instance = find_hash_in_database(pretty_hash_string)
    if not db_instance:
        return pretty_hash_string
    else:
        destroy_collision(hash_string, x + 1, y + 1)


def find_hash_in_database(string: str) -> Link:
    """
    Function that find generated_hash in database
    """
    return Link.query.filter_by(generated_hash=string).first()


def save_hash(long_link, short_hash, lifetime: int):
    new_link = Link(entered_link=long_link, generated_hash=short_hash, hash_lifetime=lifetime)
    db.session.add(new_link)
    db.session.commit()
