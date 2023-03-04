import secrets
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits


class PasswordGenerator:
    """Class for generating passwords"""
    
    def __init__(self, password_length: int, types_of_characters: list[str] | str):
        """parameterize password

        Args:
            * password_length (int): Length of the password
            * types_of_characters (list[str]): Character types of characters, default equals ["digits", "lowercase", "uppercase"]
        """
        self.__password_length: int = password_length
        self.__types_of_characters: list[str] | str = types_of_characters
        
        character_sets: dict[tuple[str], str] = {
            ('uppercase',): ascii_uppercase,
            ("lowercase",): ascii_lowercase,
            ("digits",): digits,
            ("digits", "uppercase"): ascii_uppercase + digits,
            ("digits", "lowercase"): ascii_lowercase + digits,
        }
        #stores the characters associated with the key
        self.__characters: str = character_sets.get(tuple(self.__types_of_characters) 
                                                    if isinstance(self.__types_of_characters, list) 
                                                    else (self.__types_of_characters,))
        
    def generate(self) -> str:
        """call this function to generate a random password with parameters defined in PasswordGenerator.__init__

        Returns:
            str: password generated
        """
        generation_cases: dict[tuple[str], callable] = {
            ("uppercase",): self.generate_with_uppercase,
            ("lowercase",): self.generate_with_lowercase,
            ("digits",): self.generate_with_digits,
            ("digits", "uppercase"): self.generate_with_uppercase,
            ("digits", "lowercase"): self.generate_with_lowercase,            
        }
        #returns the method call associated with the key, otherwise returns self.generate_with_all_characters
        return generation_cases.get(tuple(self.__types_of_characters) 
                                    if isinstance(self.__types_of_characters, list) 
                                    else (self.__types_of_characters,), self.generate_with_all_characters)()
    

    def generate_with_uppercase(self) -> str:
        """method to generate password only with characters uppercase

        Returns:
            str: password with uppercase
        """
        return "".join(secrets.choice(self.__characters) for password_position in range(self.__password_length))
    
    def generate_with_lowercase(self) -> str:
        """method to generate password only with characters lowercase

        Returns:
            str: password with lowercase
        """
        return "".join(secrets.choice(self.__characters) for password_position in range(self.__password_length))
    
    def generate_with_digits(self) -> str:
        """method to generate password only with digits

        Returns:
            str: _description_
        """
        return "".join(secrets.choice(self.__characters) for password_position in range(self.__password_length))
    
    def generate_with_all_characters(self) -> str:
        """method to generate password with all characters

        Returns:
            str: passwords generated with all characters
        """
        other_characters = ascii_letters + digits
        return "".join(secrets.choice(other_characters) for password_position in range(self.__password_length))
        
    def __str__(self):
        return self.generate()