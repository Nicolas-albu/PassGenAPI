from app.generator.password_generator import PasswordGenerator


def test_generate_with_all_characters():
    generated_password = PasswordGenerator(10, ["digits", "lowercase", "uppercase"])
    password = generated_password.generate_with_all_characters()
    assert password is not None
    assert len(password) == 10
    assert any(position.isdigit() for position in password)
    assert any(position.islower() for position in password)
    assert any(position.isupper() for position in password)
    
def test_generate_with_all_characters_two():
    generated_password = PasswordGenerator(15, ["lowercase", "digits", "uppercase"])
    password = generated_password.generate_with_all_characters()
    assert len(password) == 15
    assert any(position.isdigit() for position in password)
    assert any(position.islower() for position in password)
    assert any(position.isupper() for position in password)

def test_generate_with_digits():
    generated_password = PasswordGenerator(5, "digits")
    password = generated_password.generate_with_digits()
    assert len(password) == 5
    assert password.isdigit()

def test_generate_with_uppercase():
    generated_password = PasswordGenerator(7, "uppercase")
    password = generated_password.generate_with_uppercase()
    assert len(password) == 7
    assert password.isupper()

def test_generate_with_lowercase():
    generated_password = PasswordGenerator(8, "lowercase")
    password = generated_password.generate_with_lowercase()
    assert len(password) == 8
    assert password.islower()

def test_generate():
    generated_password = PasswordGenerator(12, ["digits", "lowercase"])
    password = generated_password.generate()
    assert len(password) == 12
    assert password.isalnum()
    
def test_generate_two():
    generated_password = PasswordGenerator(13, ["lowercase", "digits"])
    password = generated_password.generate()
    assert len(password) == 13
    assert password.isalnum()
    
if __name__ == "__main__":
    test_generate_with_all_characters()