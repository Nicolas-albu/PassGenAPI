from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
import secrets

class PasswordGenerator:
    """Class for generating passwords"""
    
    def __init__(self, password_length: int, types_of_characters: list[str] | str):
        """parameterize password

        Args:
            * password_length (int): Length of the password
            * types_of_characters (list[str]): Character types of characters, default equals ["uppercase", "lowercase", "digits"]
        """
        self.__password_length: int = password_length
        self.__types_of_characters: list[str] | str = types_of_characters # default is ["uppercase", "lowercase", "digits"]
        
    def generate(self) -> str:
        """call this function to generate a random password with parameters defined in PasswordGenerator.__init__

        Returns:
            str: password generated
        """
        if self.__types_of_characters == "uppercase":
            return self.generate_with_uppercase()
        elif self.__types_of_characters == "lowercase":
            return self.generate_with_lowercase()
        elif self.__types_of_characters == "digits":
            return self.generate_with_digits()
        return self.generate_with_all_characters()
    
    def generate_with_uppercase(self) -> str:
        """method to generate password only with characters uppercase

        Returns:
            str: password with uppercase
        """
        return "".join(secrets.choice(ascii_uppercase)
                       for size in range(self.__password_length))
    
    def generate_with_lowercase(self) -> str:
        """method to generate password only with characters lowercase

        Returns:
            str: password with lowercase
        """
        return "".join(secrets.choice(ascii_lowercase) 
                       for size in range(self.__password_length))
    
    def generate_with_digits(self) -> str:
        """method to generate password only with digits

        Returns:
            str: _description_
        """        """"""
        return "".join(secrets.choice(digits) 
                       for size in range(self.__password_length))
    
    def generate_with_all_characters(self) -> str:
        """method to generate password with all characters

        Returns:
            str: passwords generated with all characters
        """
        __alphabet_and_digits: str = ascii_letters + digits
        return "".join(secrets.choice(__alphabet_and_digits) 
                       for size in range(self.__password_length))
        
    def __str__(self):
        return self.generate()