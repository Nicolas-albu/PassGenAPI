from fastapi import APIRouter

from app.generator.password_generator import PasswordGenerator
from app.routes.models.password_model import Password

password_routes = APIRouter()

@password_routes.post("/password_definitions/")
async def password_generator(password_definitions: Password) -> dict:
    """Router POST method to create a new password with the passed parameters

    Args:
        password_definitions (Password): parameters for the new password

    Returns:
        dict: the new password generated in JSON format
    """
    return {
            "password": PasswordGenerator(
                password_length=password_definitions.password_length,
                types_of_characters=password_definitions.types_of_characters
                ).generate()
            }