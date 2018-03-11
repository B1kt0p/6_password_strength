import re
import string


def check_pwd_length_and_whitespace(pwd):
    if not (' ' in pwd):
        min_length_pwd = 6
        max_length_pwd = 24
        if min_length_pwd <= len(pwd) <= max_length_pwd:
            return len(pwd)


def is_pwd_in_ignor_pwd_list(pwd):
    with open('ignor_pwd', 'r', encoding='utf-8') as file:
        ignor_pwd_list = [ignor_pwd.rstrip() for ignor_pwd in file.readlines()]
    return pwd in ignor_pwd_list


def clear_duplicate_symbol(pwd):
    simbol_pwd_list = [pwd[0]]
    for index in range(1, len(pwd)):
        if not pwd[index] == pwd[index - 1]:
            simbol_pwd_list.append(pwd[index])
    return ''.join(simbol_pwd_list)


def count_lower_letters(pwd):
    number_lower_letters = sum(
        [1 for char in pwd if char.isalpha() and char.islower()]
    )
    return number_lower_letters


def count_upper_letters(pwd):
    number_upper_letters = sum(
        [1 for char in pwd if char.isalpha() and char.isupper()]
    )
    return number_upper_letters


def count_digits(pwd):
    number_digits = sum(
        [1 for char in pwd if char.isdigit()]
    )
    return number_digits


def count_spec_symbol(pwd):
    symbol_list = re.findall(r'[{}]'.format(string.punctuation), pwd)
    return len(symbol_list)


def appreciate_symbol_in_pwd(number_symbol):
    max_rating = 2
    min_rating = 1
    if number_symbol > 1:
        return max_rating
    elif number_symbol == 1:
        return min_rating
    return 0


def password_len_rating(pwd):
    max_rating = 2
    min_rating = 1
    len_pwd = len(pwd)
    if len_pwd >= 18:
        return max_rating
    elif len_pwd >= 12:
        return min_rating
    return 0


def get_password_strength(pwd):
    rating_pwd = 0
    rating_pwd += password_len_rating(pwd)
    pwd = clear_duplicate_symbol(pwd)
    number_lower_letters = count_lower_letters(pwd)
    number_upper_letters = count_upper_letters(pwd)
    number_digits = count_digits(pwd)
    number_spec_symbol = count_spec_symbol(pwd)
    for number_symbol in number_lower_letters, number_upper_letters, number_digits, number_spec_symbol:
        rating_pwd += appreciate_symbol_in_pwd(number_symbol)
    return rating_pwd


def main():
    while True:
        pwd = input(
            'Enter the password (from 6 to 24 characters) or "quit" to exit: '
        )
        if pwd == 'quit':
            print ('The script is completed')
            break
        elif is_pwd_in_ignor_pwd_list(pwd) or not check_pwd_length_and_whitespace(pwd):
            print('Invalid password entered!')
            continue
        password_strength = get_password_strength(pwd)
        print(
            'Password rating {} points from 10 points.'.format(
                password_strength
            )
        )


if __name__ == '__main__':
    main()
