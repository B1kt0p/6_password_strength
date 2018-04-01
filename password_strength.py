import re
import string
import getpass


def check_password_length(password):
    min_length_password = 6
    max_length_password = 32
    if min_length_password <= len(password) <= max_length_password:
        return len(password)


def load_black_list():
    with open('blacklist', 'r', encoding='utf-8') as file:
        ignor_password_list = [
            ignor_password.rstrip() for ignor_password in file.readlines()
        ]
    return ignor_password_list


def is_pasword_ignor(password, black_list):
    return password in black_list


def clear_duplicate_symbols(password):
    return ''.join(set(password))


def get_lowercase_letters_count(password):
    number_lower_letters = sum(
        [1 for char in password if char.islower()]
    )
    return number_lower_letters


def get_uppercase_letters_count(password):
    number_upper_letters = sum(
        [1 for char in password if char.isupper()]
    )
    return number_upper_letters


def get_digits_count(password):
    number_digits = sum(
        [1 for char in password if char.isdigit()]
    )
    return number_digits


def get_spec_symbol_count(password):
    symbol_list = re.findall(r'[{}]'.format(string.punctuation), password)
    return len(symbol_list)


def get_symbols_rating(number_symbol):
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
    password = clear_duplicate_symbols(password)
    number_lowercase_letters = get_lowercase_letters_count(password)
    number_uppercase_letters = get_uppercase_letters_count(password)
    number_digits = get_digits_count(password)
    number_spec_symbol = get_spec_symbol_count(password)
    for number_symbol in [number_lowercase_letters,
                          number_uppercase_letters,
                          number_digits,
                          number_spec_symbol
                          ]:
        rating_password += get_symbols_rating(number_symbol)
    return rating_password


if __name__ == '__main__':
    password = getpass.getpass('Enter the password (from 6 to 24 characters): ')
    pasword_ignor = is_pasword_ignor(password, load_black_list())
    if pasword_ignor or not check_password_length(password):
        exit('Invalid password entered!')
    password_strength = get_password_strength(password)
    print(
        'Password rating {} points from 10 points.'.format(password_strength)
    )
