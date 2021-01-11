from .models import Link
from .prapare import find_hash_in_database, create_hash, save_hash
from flask_restful import abort
from .validator import link_data_validation
import webbrowser


def short_link(link_data: dict) -> tuple:
    """
    Write your application url(protocol://prefix.domain.domain_zone)
    in current_app string variable
    example: current_app = 'https://bigtech-company.com/'
    """
    current_app = 'http://localhost:5000/'
    validation = link_data_validation()

    if validation.validate(link_data):
        entered_link = link_data['link']
        lifetime = link_data['lifetime']
        link = Link.query.filter_by(entered_link=entered_link).first()
        if not link:
            hash_string = create_hash(entered_link)
            save_hash(entered_link, hash_string, lifetime)
            return {'message': 'Successfully shortened.',
                    'short_link': f'{current_app}{hash_string}'}, 201
        else:
            return {'message': 'Already shortened.',
                    'short_link': f'{current_app}{link.generated_hash}'}, 201
    else:
        return validation.errors, 400


def link_redirection(hash_link):
    link_instance = find_hash_in_database(hash_link)
    if link_instance:
        return webbrowser.open(link_instance.entered_link)
    else:
        abort(400)
