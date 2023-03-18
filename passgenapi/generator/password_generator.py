import secrets
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import Union


class PasswordGenerator:
    """Class for generating passwords"""

    def __init__(
        self,
        password_length: int,
        number_of_passwords: int,
        types_of_characters: Union[list[str], str],
    ):
        """parameterize password

        Args:
            * password_length (int): Length of the password
            * types_of_characters (list[str]): Character types of characters,
              default equals ["digits", "lowercase", "symbols", "uppercase"]
        """
        # Parameter validation
        if types_of_characters is None:
            types_of_characters = ["digits", "lowercase", "symbols", "uppercase"]

        # attribute definition
        self.__password_length: int = password_length
        self.__number_of_passwords: int = number_of_passwords
        self.__types_of_characters: tuple[str] = tuple(
            sorted(
                types_of_characters
                if isinstance(types_of_characters, list)
                else [types_of_characters]
            )
        )
        self.__character_sets: dict[str, str] = {
            "uppercase": ascii_uppercase,
            "lowercase": ascii_lowercase,
            "symbols": punctuation,
            "digits": digits,
        }
        self.__character_final: str = ""

        # get all groups of characters from the type_of_characters parameter
        parameter_character_sets: list[Union[str, None]] = [
            self.__character_sets.get(character_parameter)
            for character_parameter in self.__types_of_characters
        ]
        # concatenate all character sets associated with the braces in __character_final
        self.__character_final = "".join(filter(None, parameter_character_sets))

    def __verify_has_digits_lower_upper(self, password: str) -> bool:
        """method private to check if password has digits, characters lower and upper

        Args:
            password (str): password to be checked

        Returns:
            bool: verified password boolean value
        """
        __has_digit: bool = any(position.isdigit() for position in password)
        __has_lower: bool = any(position.islower() for position in password)
        __has_upper: bool = any(position.isupper() for position in password)
        return __has_digit and __has_lower and __has_upper

    def __verify_has_symbols(self, password: str) -> bool:
        """private method to check if password has symbols

        Args:
            password (str): password to be checked

        Returns:
            bool: verified password boolean value
        """
        __has_symbols: bool = any(position in punctuation for position in password)
        return __has_symbols

    def generate_password(self) -> Union[list[str], str]:
        """call this method to generate a random password with parameters defined in the
           PasswordGenerator instantiation

        Returns:
            str: password generated
        """
        generation_cases: dict = {
            self.__types_of_characters: self.generate_defined_password,
        }
        # method call associated with the key, otherwise returns self.generate_full_character_password
        __password_generated: str = generation_cases.get(
            self.__types_of_characters, self.generate_full_character_password
        )
        __list_of_passwords: list[str] = [
            __password_generated()
            for number in range(self.__number_of_passwords)
            if self.__number_of_passwords >= 1
        ]
        return (
            __list_of_passwords[0]
            if len(__list_of_passwords) == 1
            else __list_of_passwords
        )

    def generate_defined_password(self) -> str:
        """method to generate passwords with definitions of characters of method generate_password()

        Returns:
            str: password generated
        """
        return "".join(
            secrets.choice(self.__character_final)
            for password_position in range(self.__password_length)
        )

    def generate_full_character_password(self) -> str:
        """method to generate password with all characters

        Returns:
            str: passwords generated with all characters
        """
        __password_with_all_characters: str = "".join(
            secrets.choice(self.__character_final)
            for password_position in range(self.__password_length)
        )

        # 4 is the minimum quantity to have all the characters
        if self.__password_length >= 4:
            # as long as the password has no lowercase, uppercase, digits and symbols, generate password
            while not (
                self.__verify_has_digits_lower_upper(__password_with_all_characters)
                and self.__verify_has_symbols(__password_with_all_characters)
            ):
                __password_with_all_characters = "".join(
                    secrets.choice(self.__character_final)
                    for password_position in range(self.__password_length)
                )
        return __password_with_all_characters

    def __str__(self):
        return self.generate_password()
