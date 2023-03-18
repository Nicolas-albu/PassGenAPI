from fastapi import APIRouter

from passgenapi.generator.password_generator import PasswordGenerator
from passgenapi.routes.models.password_model import PasswordModel

password_routes = APIRouter()

@password_routes.post("/password/")
async def post_password_generator(password_definitions: PasswordModel) -> dict:
    """Router POST method to create a new password with the passed parameters

    Args:
        password_definitions (Password): parameters for the new password

    Returns:
        dict: the new password generated in JSON format
    """
    return {
            "password": PasswordGenerator(
                        password_length=password_definitions.password_length,
                        number_of_passwords=password_definitions.number_of_passwords,
                        types_of_characters=password_definitions.types_of_characters
                        ).generate_password()
            }