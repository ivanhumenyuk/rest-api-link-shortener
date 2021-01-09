import random


def hash_prettier(_hash: str):
    hash_string = _hash.replace('0', '1')
    pretty_hash_string = ''

    for letter in hash_string:
        if letter.isdigit():
            if random.randint(1, 2) == 1:
                new_upper_letter = chr(ord('@') + int(letter))
                pretty_hash_string += new_upper_letter
            else:
                new_lower_letter = chr(ord('`') + int(letter))
                pretty_hash_string += new_lower_letter
        else:
            if letter.isupper():
                new_str_digit_from_upper = str(ord(letter) - 64)
                pretty_hash_string += new_str_digit_from_upper
            else:
                new_str_digit_from_lower = str(ord(letter) - 96)
                pretty_hash_string += new_str_digit_from_lower
    return pretty_hash_string





