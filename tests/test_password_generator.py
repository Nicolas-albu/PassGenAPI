from app.generator.password_generator import PasswordGenerator


def test_generate_full_character_password():
    generated_password = PasswordGenerator(10, ["digits", "lowercase", "uppercase"])
    password = generated_password.generate_full_character_password()
    assert password is not None
    assert len(password) == 10
    assert any(position.isdigit() for position in password)
    assert any(position.islower() for position in password)
    assert any(position.isupper() for position in password)
    
def test_generate_full_character_password_two():
    generated_password = PasswordGenerator(15, ["lowercase", "digits", "uppercase"])
    password = generated_password.generate_full_character_password()
    assert len(password) == 15
    assert any(position.isdigit() for position in password)
    assert any(position.islower() for position in password)
    assert any(position.isupper() for position in password)

def test_generate_password_with_digits():
    generated_password = PasswordGenerator(5, "digits")
    password = generated_password.generate_defined_password()
    assert len(password) == 5
    assert password.isdigit()

def test_generate_password_with_uppercase():
    generated_password = PasswordGenerator(7, "uppercase")
    password = generated_password.generate_defined_password()
    assert len(password) == 7
    assert password.isupper()

def test_generate_password_with_lowercase():
    generated_password = PasswordGenerator(8, "lowercase")
    password = generated_password.generate_defined_password()
    assert len(password) == 8
    assert password.islower()

def test_generate_password():
    generated_password = PasswordGenerator(12, ["digits", "lowercase"])
    password = generated_password.generate_password()
    assert len(password) == 12
    assert password.isalnum()
    assert not password.isupper()
    
def test_generate_password_two():
    generated_password = PasswordGenerator(13, ["lowercase", "digits"])
    password = generated_password.generate_password()
    assert len(password) == 13
    assert password.isalnum()
    assert password.islower()
    assert not password.isupper()
    
def test_generate_password_three():
    generated_password = PasswordGenerator(12, ["digits", "uppercase", "lowercase"])
    password = generated_password.generate_password()
    assert len(password) == 12
    assert password.isalnum()
    assert not password.isupper()
    
def test_generate_password_four():
    generated_password = PasswordGenerator(12, ["digits", "lowercase", "uppercase"])
    password = generated_password.generate_password()
    assert len(password) == 12
    assert password.isalnum()
    assert not password.isupper()