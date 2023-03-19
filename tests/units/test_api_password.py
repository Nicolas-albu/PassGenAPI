import json
from string import punctuation
from typing import Union

import requests

endpoint = "https://pass-gen-api.vercel.app/password"


def get_response(password_data: dict[str, Union[int, str, list[str]]]):
    # Convert data to JSON format
    json_password_data = json.dumps(password_data)

    # Send POST request to API endpoint with data in JSON
    response = requests.post(url=endpoint, data=json_password_data)

    return response.json()["password"]


def get_assert(password):
    symbols = any(symbol in punctuation for symbol in password)
    digits = any(position.isdigit() for position in password)
    lowers = any(position.islower() for position in password)
    uppers = any(position.isupper() for position in password)
    return symbols, digits, lowers, uppers


def test_full_character_password():
    password_data = {
        "password_length": 10,
        "number_of_passwords": 1,
        "types_of_characters": ["digits", "lowercase", "symbols", "uppercase"],
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 10
    assert get_assert(password)


def test_generate_full_character_password_list():
    password_data = {
        "password_length": 10,
        "number_of_passwords": 4,
        "types_of_characters": ["digits", "lowercase", "symbols", "uppercase"],
    }
    assert (list_of_passwords := get_response(password_data)) is not None
    assert len(list_of_passwords) == 4
    assert any(len(password) == 10 for password in list_of_passwords)
    assert any(
        symbol in punctuation for password in list_of_passwords for symbol in password
    )
    assert any(
        position.isdigit() for password in list_of_passwords for position in password
    )
    assert any(
        position.islower() for password in list_of_passwords for position in password
    )
    assert any(
        position.isupper() for password in list_of_passwords for position in password
    )


def test_second_generate_full_character_password():
    password_data = {
        "password_length": 23,
        "number_of_passwords": 1,
        "types_of_characters": ["symbols", "lowercase", "digits", "uppercase"],
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 23
    assert get_assert(password)


def test_third_generate_full_character_password():
    password_data = {
        "password_length": 15,
        "number_of_passwords": 1,
        "types_of_characters": ["digits", "lowercase", "symbols", "uppercase"],
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 15
    assert get_assert(password)


def test_fourth_generate_full_character_password():
    password_data = {
        "password_length": 34,
        "number_of_passwords": 1,
        "types_of_characters": ["uppercase", "lowercase", "digits", "symbols"],
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 34
    assert get_assert(password)


def test_generate_password_with_symbols():
    password_data = {
        "password_length": 20,
        "number_of_passwords": 1,
        "types_of_characters": ["uppercase", "lowercase", "digits", "symbols"],
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 20
    assert get_assert(password)


def test_generate_password_with_digits():
    password_data = {
        "password_length": 5,
        "number_of_passwords": 1,
        "types_of_characters": "digits",
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 5
    assert password.isdigit()
    assert not any(symbol in punctuation for symbol in password)
    assert not any(position.islower() for position in password)
    assert not any(position.isupper() for position in password)


def test_generate_password_with_uppercase():
    password_data = {
        "password_length": 7,
        "number_of_passwords": 1,
        "types_of_characters": "uppercase",
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 7
    assert password.isupper()
    assert not any(symbol in punctuation for symbol in password)
    assert not any(position.isdigit() for position in password)
    assert not any(position.islower() for position in password)


def test_generate_password_with_lowercase():
    password_data = {
        "password_length": 8,
        "number_of_passwords": 1,
        "types_of_characters": "lowercase",
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 8
    assert password.islower()
    assert not any(symbol in punctuation for symbol in password)
    assert not any(position.isdigit() for position in password)
    assert not any(position.isupper() for position in password)


def test_generate_password():
    password_data = {
        "password_length": 12,
        "number_of_passwords": 1,
        "types_of_characters": ["digits", "lowercase"],
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 12
    assert password.isalnum()
    assert not password.isupper()
    assert not any(symbol in punctuation for symbol in password)
    assert not any(position.isupper() for position in password)


def test_generate_password_two():
    password_data = {
        "password_length": 13,
        "number_of_passwords": 1,
        "types_of_characters": ["lowercase", "digits"],
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 13
    assert password.isalnum()
    assert password.islower()
    assert not any(position.isupper() for position in password)


def test_generate_password_with_symbols():
    password_data = {
        "password_length": 20,
        "number_of_passwords": 1,
        "types_of_characters": "symbols",
    }
    assert (password := get_response(password_data)) is not None
    assert len(password) == 20
    assert any(symbol in punctuation for symbol in password)
