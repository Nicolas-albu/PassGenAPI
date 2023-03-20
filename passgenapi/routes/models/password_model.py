"""This module contains the parameter template for the password generation POST route."""

from typing import Union

from pydantic import BaseModel, validator


class PasswordModel(BaseModel):
    """JSON parameter model class to generate password.

    Args:
        * BaseModel (pydantic.BaseModel): Password template for the parameters of a JSON request from endpoint /password_definitions/
        * password_length (int): Length of the password
        * type_of_characters (list[str] | None): Character types, default equals ["digits", "lowercase", "symbols", "uppercase"]
    """

    password_length: int = 12
    number_of_passwords: int = 1
    types_of_characters: Union[list[str], str] = None

    @validator("types_of_characters")
    def not_none_in_types_of_characters(cls, character):
        return (
            ["digits", "lowercase", "symbols", "uppercase"]
            if character in (None, "")
            else character
        )

    @validator("types_of_characters")
    def convert_type_of_characters(cls, list_of_characters):
        return tuple(
            sorted(
                list_of_characters
                if isinstance(list_of_characters, list)
                else [list_of_characters]
            )
        )
