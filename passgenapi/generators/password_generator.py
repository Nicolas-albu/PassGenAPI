"""This module contains the PasswordGenerator class for generating passwords."""

import secrets
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import Generator


class PasswordGenerator:
    """Class for generating passwords."""

    def __init__(
        self,
        password_length: int,
        number_of_passwords: int,
        types_of_characters: tuple[str],
    ):
        """Parameterize password.

        Args:
            * password_length (int): Length of the password
            * types_of_characters (list[str] | str): Character types,
              default equals ["digits", "lowercase", "symbols", "uppercase"]
        """
        self.__password_length: int = password_length
        self.__number_of_passwords: int = number_of_passwords
        self.__types_of_characters: tuple[str] = types_of_characters
        self.__character_sets: dict[str, str] = {
            "digits": digits,
            "lowercase": ascii_lowercase,
            "symbols": punctuation,
            "uppercase": ascii_uppercase,
        }
        self.__character_final: str = ""

        # concatenate all character sets associated with character types
        self.__character_final = "".join(
            self.__character_sets.get(character_parameter)
            for character_parameter in self.__types_of_characters
        )

    def generate_password(self) -> tuple:
        """Call this method to generate a random password with parameters defined in the PasswordGenerator instantiation.

        Returns:
            str: password generated
        """
        # method call associated with character types, otherwise returns self.generate_full_character_password
        __password_generated: str = (
            self.generate_defined_password
            if len(self.__types_of_characters) != 4  # max size of char types
            else self.generate_full_character_password
        )
        __passwords: Generator = (
            __password_generated()
            for number in range(self.__number_of_passwords)
        )
        return __passwords

    def generate_defined_password(self) -> str:
        """Generate passwords with definitions of characters of method generate_password().

        Returns:
            str: password generated
        """
        return "".join(
            secrets.choice(self.__character_final)
            for password_position in range(self.__password_length)
        )

    def generate_full_character_password(self) -> str:
        """Generate password with all characters.

        Returns:
            str: passwords generated with all characters
        """

        @staticmethod
        def verify_has_digits_lower_upper(password: str) -> bool:
            """Check if password has digits, characters lower and upper.

            Args:
                password (str): password to be checked

            Returns:
                bool: verified password boolean value
            """
            __has_digit: bool = any(
                position.isdigit() for position in password
            )
            __has_lower: bool = any(
                position.islower() for position in password
            )
            __has_upper: bool = any(
                position.isupper() for position in password
            )
            return __has_digit and __has_lower and __has_upper

        @staticmethod
        def verify_has_symbols(password: str) -> bool:
            """Check if password has symbols.

            Args:
                password (str): password to be checked

            Returns:
                bool: verified password boolean value
            """
            __has_symbols: bool = any(
                position in punctuation for position in password
            )
            return __has_symbols

        __password_with_all_characters: str = "".join(
            secrets.choice(self.__character_final)
            for password_position in range(self.__password_length)
        )

        # 4 is the minimum quantity to have all the characters
        if self.__password_length >= 4:
            # as long as the password has no lowercase, uppercase, digits and symbols, generate password
            while not (
                verify_has_digits_lower_upper(__password_with_all_characters)
                and verify_has_symbols(__password_with_all_characters)
            ):
                __password_with_all_characters = "".join(
                    secrets.choice(self.__character_final)
                    for password_position in range(self.__password_length)
                )
        return __password_with_all_characters

    def __str__(self):
        """Return a password generated with passed parameters.

        Returns:
            _type_: generated password
        """
        return self.generate_password()
