import re
import string
import getpass
from collections import OrderedDict


def check_password_length_and_whitespace(password):
    if not (' ' in password):
        min_length_password = 6
        max_length_password = 24
        if min_length_password <= len(password) <= max_length_password:
            return len(password)


def get_ignor_password_list():
    with open('ignor_password', 'r', encoding='utf-8') as file:
        ignor_password_list = [
            ignor_password.rstrip()
            for ignor_password in file.readlines()
        ]
    return ignor_password_list


def is_pasword_ignor(password, ignor_password_list):
    return password in ignor_password_list


def clear_duplicate_symbol(password):
    return "".join(OrderedDict.fromkeys(password))


def get_number_lowercase_letters(password):
    number_lower_letters = sum(
        [1 for char in password if char.islower()]
    )
    return number_lower_letters


def get_number_uppercase_letters(password):
    number_upper_letters = sum(
        [1 for char in password if char.isupper()]
    )
    return number_upper_letters


def get_number_digits(password):
    number_digits = sum(
        [1 for char in password if char.isdigit()]
    )
    return number_digits


def get_number_spec_symbol(password):
    symbol_list = re.findall(r'[{}]'.format(
        string.punctuation), password
    )
    return len(symbol_list)


def appreciate_symbol_in_password(number_symbol):
    max_rating = 2
    min_rating = 1
    if number_symbol > 1:
        return max_rating
    elif number_symbol == 1:
        return min_rating
    return 0


def password_len_rating(password):
    max_rating = 2
    min_rating = 1
    len_password = len(password)
    if len_password >= 18:
        return max_rating
    elif len_password >= 12:
        return min_rating
    return 0


def get_password_strength(password):
    rating_password = 0
    rating_password += password_len_rating(password)
    password = clear_duplicate_symbol(password)
    number_lowercase_letters = get_number_lowercase_letters(password)
    number_uppercase_letters = get_number_uppercase_letters(password)
    number_digits = get_number_digits(password)
    number_spec_symbol = get_number_spec_symbol(password)
    for number_symbol in [number_lowercase_letters,
                          number_uppercase_letters,
                          number_digits,
                          number_spec_symbol
                          ]:
        rating_password += appreciate_symbol_in_password(number_symbol)
    return rating_password


if __name__ == '__main__':
    password = getpass.getpass(
        'Enter the password (from 6 to 24 characters) or "quit" to exit: '
    )
    if password == 'quit':
        print('The script is completed')
    elif is_pasword_ignor(password, get_ignor_password_list()) or not check_password_length_and_whitespace(password):
        print('Invalid password entered!')
    password_strength = get_password_strength(password)
    print(
        'Password rating {} points from 10 points.'.format(
            password_strength
        )
    )
