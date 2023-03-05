import secrets
from string import (ascii_letters, ascii_lowercase, ascii_uppercase, digits,
                    punctuation)


class PasswordGenerator:
    """Class for generating passwords"""
    
    def __init__(self, password_length: int, types_of_characters: list[str] | str):
        """parameterize password

        Args:
            * password_length (int): Length of the password
            * types_of_characters (list[str]): Character types of characters, default equals ["digits", "lowercase", "symbols", "uppercase"]
        """
        self.__password_length: int = password_length
        self.__types_of_characters: list[str] = types_of_characters if isinstance(types_of_characters, list) else [types_of_characters]
        self.__types_of_characters.sort()
        
        self.__all_characters: str = ascii_letters + digits + punctuation
        self.__character_sets: dict[tuple[str], str] = {
            ("digits", "uppercase"): ascii_uppercase + digits,
            ("digits", "lowercase"): ascii_lowercase + digits,
            ("lowercase", "uppercase"): ascii_letters,
            ("uppercase",): ascii_uppercase,
            ("lowercase",): ascii_lowercase,
            ("symbols",): punctuation,
            ("digits",): digits,
        }
        #stores the characters associated with the key
        self.__characters: str = self.__character_sets.get(tuple(self.__types_of_characters), self.__all_characters)
        
    def generate_password(self) -> str:
        """call this function to generate a random password with parameters defined in PasswordGenerator.__init__

        Returns:
            str: password generated
        """
        generation_cases: dict = {
            tuple(self.__types_of_characters): self.generate_defined_password,
        }
        #returns the method call associated with the key, otherwise returns self.generate_full_character_password
        return generation_cases.get(tuple(self.__types_of_characters), self.generate_full_character_password)()
    
    def generate_defined_password(self) -> str:
        """method to generate passwords with definitions of characters of method generate_password()

        Returns:
            str: password generated
        """      
        return "".join(secrets.choice(self.__characters) for password_position in range(self.__password_length))
    
    def generate_full_character_password(self) -> str:
        """method to generate password with all characters

        Returns:
            str: passwords generated with all characters
        """
        __password: str = "".join(secrets.choice(self.__all_characters) for password_position in range(self.__password_length))

        while not (any(position.isdigit() for position in __password) and 
                   any(symbol in punctuation for symbol in __password)):
            __password = "".join(secrets.choice(self.__all_characters) for password_position in range(self.__password_length))
        return __password
        
    def __str__(self):
        return self.generate_password()