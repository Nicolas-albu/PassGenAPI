from pydantic import BaseModel


class PasswordModel(BaseModel):
    """JSON parameter model class to generate password

    Args:
        * BaseModel (pydantic.BaseModel): Password template for the parameters of a JSON request from endpoint /password_definitions/
        * password_length (int): Length of the password
        * type_of_characters (list[str] | None): Character types, default equals ["digits", "lowercase", "symbols", "uppercase"]
    """
    password_length: int = 12
    number_of_passwords: int = 1
    types_of_characters: list[str] | str | None = ["digits", "lowercase", "symbols", "uppercase"]