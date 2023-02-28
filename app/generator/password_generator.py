import secrets
import string

class PasswordGenerator():
    def __init__(self, password_length: int, types_of_characters: list[str]):
        self.__password_length: int = password_length
        self.__types_of_characters: list[str] = types_of_characters # default is ["uppercase", "lowercase", "digits"]
        
    def generate(self) -> str | None:
        if self.__types_of_characters == ['uppercase', 'lowercase', 'digits']:
            return self.generate_with_all_characters()
    
    def generate_with_all_characters(self) -> str:
        __alphabet_and_digits: str = string.ascii_letters + string.digits
        return "".join(secrets.choice(__alphabet_and_digits) 
                       for size in range(self.__password_length))
        
    def generate_with_uppercase(self) -> str:
        ...
        
    def generate_with_lowercase(self) -> str:
        ...
        
    def generate_with_digits(self) -> str:
        ...
        
    def __repr__():
        return "PasswordGenerator(password_length: int, types_of_characters: list[str])"