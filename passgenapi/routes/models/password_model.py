"""This module contains the parameter template for the password generation POST route."""

from typing import Any, Optional

from pydantic import BaseModel, validator

from ...errors import PasswordNumberLessThanZeroError

DEFAULT_TYPES_OF_CHARACTERS: tuple[str] = (
    "digits",
    "lowercase",
    "symbols",
    "uppercase",
)


class PasswordModel(BaseModel):
    """JSON parameter model class to generate password.

    Args:
        * BaseModel (pydantic.BaseModel): Password template for the parameters of a JSON request from endpoint /password_definitions/
        * password_length (int): Length of the password
        * type_of_characters (tuple[str] | list[str] | str | None): Character types, default equals ("digits", "lowercase", "symbols", "uppercase")
    """

    password_length: int = 12
    number_of_passwords: int = 1
    types_of_characters: Optional[
        tuple[str] | list[str] | str
    ] = DEFAULT_TYPES_OF_CHARACTERS

    @validator("number_of_passwords")
    def cannot_be_less_than_zero(cls, value: int):
        if value <= 0:
            raise PasswordNumberLessThanZeroError()
        return value

    @validator("types_of_characters")
    def convert_if_types_of_characters_is_none(cls, types_chars: None) -> dict:
        if types_chars is None:
            types_chars = DEFAULT_TYPES_OF_CHARACTERS
        return types_chars

    @validator("types_of_characters")
    def convert_types_of_characters_to_tuple(cls, types_chars: str | list[str]) -> tuple[str]:
        """Converts the value of the type_of_character parameter to a tuple.

        Args:
            types_chars (str | list[str]): types_of_characters

        Returns:
            tuple: types_of_characters as tuple
        """
        if isinstance(types_chars, list):
            return tuple(sorted(types_chars))

        elif isinstance(types_chars, str):
            return (types_chars,)
