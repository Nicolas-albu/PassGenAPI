"""This module contains the parameter template for the password generation POST route."""

from typing import Union

from pydantic import BaseModel, root_validator, validator

from ...errors import PasswordNumberLessThanZeroError


class PasswordModel(BaseModel):
    """JSON parameter model class to generate password.

    Args:
        * BaseModel (pydantic.BaseModel): Password template for the parameters of a JSON request from endpoint /password_definitions/
        * password_length (int): Length of the password
        * type_of_characters (list[str] | str): Character types, default equals ["digits", "lowercase", "symbols", "uppercase"]
    """

    password_length: int = 12
    number_of_passwords: int = 1
    types_of_characters: Union[list[str], str] = (
        "digits",
        "lowercase",
        "symbols",
        "uppercase",
    )

    @validator('number_of_passwords')
    def cannot_be_less_than_zero(cls, value: int): 
        if value <= 0:
            raise PasswordNumberLessThanZeroError()
        return value

    @root_validator
    def convert_types_of_characters_to_tuple(cls, parameters: dict) -> dict:
        """Converts the value of the type_of_character parameter to a tuple.

        Args:
            parameters (dict): parameters in dictionary

        Returns:
            dict: parameters with types_of_characters as tuple
        """

        types_of_chars: Union[tuple, list, str] = parameters[
            "types_of_characters"
        ]
        parameters["types_of_characters"] = (
            types_of_chars
            if isinstance(types_of_chars, tuple)
            else tuple(
                sorted(
                    types_of_chars
                    if isinstance(types_of_chars, list)
                    else [types_of_chars]
                )
            )
        )
        return parameters
