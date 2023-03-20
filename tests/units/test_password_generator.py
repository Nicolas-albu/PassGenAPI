from string import punctuation

from passgenapi.generators.password_generator import PasswordGenerator


def test_generate_full_character_password():
    generated_password = PasswordGenerator(
        10, 1, ["digits", "lowercase", "symbols", "uppercase"]
    )
    password = generated_password.generate_full_character_password()
    assert password is not None
    assert len(password) == 10
    assert any(symbol in punctuation for symbol in password)
    assert any(position.isdigit() for position in password)
    assert any(position.islower() for position in password)
    assert any(position.isupper() for position in password)


def test_generate_full_character_password_list():
    generated_password = PasswordGenerator(
        password_length=10,
        number_of_passwords=4,
        types_of_characters=["digits", "lowercase", "symbols", "uppercase"],
    )
    list_of_passwords = generated_password.generate_password()
    assert list_of_passwords is not None
    assert len(list_of_passwords) == 4
    assert any(len(password) == 10 for password in list_of_passwords)
    assert any(
        symbol in punctuation
        for password in list_of_passwords
        for symbol in password
    )
    assert any(
        position.isdigit()
        for password in list_of_passwords
        for position in password
    )
    assert any(
        position.islower()
        for password in list_of_passwords
        for position in password
    )
    assert any(
        position.isupper()
        for password in list_of_passwords
        for position in password
    )


def test_second_generate_full_character_password():
    generated_password = PasswordGenerator(
        23, 1, ["symbols", "lowercase", "digits", "uppercase"]
    )
    password = generated_password.generate_full_character_password()
    assert password is not None
    assert len(password) == 23
    assert any(symbol in punctuation for symbol in password)
    assert any(position.isdigit() for position in password)
    assert any(position.islower() for position in password)
    assert any(position.isupper() for position in password)


def test_third_generate_full_character_password():
    generated_password = PasswordGenerator(
        15, 1, ["digits", "lowercase", "symbols", "uppercase"]
    )
    password = generated_password.generate_full_character_password()
    assert password is not None
    assert len(password) == 15
    assert any(symbol in punctuation for symbol in password)
    assert any(position.isdigit() for position in password)
    assert any(position.islower() for position in password)
    assert any(position.isupper() for position in password)


def test_fourth_generate_full_character_password():
    generated_password = PasswordGenerator(
        34, 1, ["uppercase", "lowercase", "digits", "symbols"]
    )
    password = generated_password.generate_full_character_password()
    assert password is not None
    assert len(password) == 34
    assert any(symbol in punctuation for symbol in password)
    assert any(position.isdigit() for position in password)
    assert any(position.islower() for position in password)
    assert any(position.isupper() for position in password)


def test_generate_password_with_symbols():
    generated_password = PasswordGenerator(
        20, 1, ["uppercase", "lowercase", "digits", "symbols"]
    )
    password = generated_password.generate_password()
    assert password is not None
    assert len(password) == 20
    assert any(symbol in punctuation for symbol in password)


def test_generate_password_with_digits():
    generated_password = PasswordGenerator(5, 1, "digits")
    password = generated_password.generate_defined_password()
    assert password is not None
    assert len(password) == 5
    assert password.isdigit()
    assert not any(symbol in punctuation for symbol in password)
    assert not any(position.islower() for position in password)
    assert not any(position.isupper() for position in password)


def test_generate_password_with_uppercase():
    generated_password = PasswordGenerator(7, 1, "uppercase")
    password = generated_password.generate_defined_password()
    assert password is not None
    assert len(password) == 7
    assert password.isupper()
    assert not any(symbol in punctuation for symbol in password)
    assert not any(position.isdigit() for position in password)
    assert not any(position.islower() for position in password)


def test_generate_password_with_lowercase():
    generated_password = PasswordGenerator(8, 1, "lowercase")
    password = generated_password.generate_defined_password()
    assert password is not None
    assert len(password) == 8
    assert password.islower()
    assert not any(symbol in punctuation for symbol in password)
    assert not any(position.isdigit() for position in password)
    assert not any(position.isupper() for position in password)


def test_generate_password():
    generated_password = PasswordGenerator(12, 1, ["digits", "lowercase"])
    password = generated_password.generate_password()
    assert password is not None
    assert len(password) == 12
    assert password.isalnum()
    assert not password.isupper()
    assert not any(symbol in punctuation for symbol in password)
    assert not any(position.isupper() for position in password)


def test_generate_password_two():
    generated_password = PasswordGenerator(13, 1, ["lowercase", "digits"])
    password = generated_password.generate_password()
    assert password is not None
    assert len(password) == 13
    assert password.isalnum()
    assert password.islower()
    assert not any(position.isupper() for position in password)


def test_generate_password_with_symbols():
    generated_password = PasswordGenerator(20, 1, "symbols")
    password = generated_password.generate_password()
    assert password is not None
    assert len(password) == 20
    assert any(symbol in punctuation for symbol in password)
