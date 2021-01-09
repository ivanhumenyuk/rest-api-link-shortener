from .models import Link
from .utils import hash_prettier


def destroy_collision(hash_string: str, x=0, y=7):
    short_hash = hash_string[x: y]
    print(short_hash)
    pretty_hash_string = hash_prettier(short_hash)
    db_instance = Link.query.filter_by(generated_hash=pretty_hash_string).first()
    if not db_instance:
        return pretty_hash_string

    else:
        destroy_collision(hash_string, x + 1, y + 1)
