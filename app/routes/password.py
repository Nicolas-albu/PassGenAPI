from fastapi import APIRouter

from app.generator.password_generator import PasswordGenerator
from app.routes.models.password_model import Password

password_routes = APIRouter()

@password_routes.post("/password_definitions/")
def password_generator(password_definitions: Password):
    
    return {
            "password": PasswordGenerator(
                password_length=password_definitions.password_length,
                types_of_characters=password_definitions.types_of_characters
                ).generate()
            }