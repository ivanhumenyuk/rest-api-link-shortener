from cerberus import Validator


def link_data_validation():
    schema = {
        'link': {'type': 'string', 'required': True, 'minlength': 10, 'maxlength': 2048, 'nullable': False, },
        'lifetime': {'type': 'integer', 'min': 1, 'max': 365, 'required': True, 'nullable': False}
    }
    validator = Validator(schema)

    return validator
