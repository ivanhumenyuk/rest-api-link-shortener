import hashlib
from .models import Link, db
from .prapare import destroy_collision


def save_new_link(entered_link) -> tuple:
    link = Link.query.filter_by(entered_link=entered_link).first()
    if not link:
        hash_string = create_hash(entered_link)
        create_new_link(entered_link, hash_string)
        return {'short_link': hash_string}, 201
    else:
        return {'short_link': link.generated_hash}, 201


def create_hash(long_link: str):
    hash_object = hashlib.md5(long_link.encode('utf-8'))
    hash_string = hash_object.hexdigest()
    generated_hash = destroy_collision(hash_string)
    return generated_hash


def create_new_link(long_link, short_hash):
    new_link = Link(entered_link=long_link, generated_hash=short_hash)
    db.session.add(new_link)
    db.session.commit()

