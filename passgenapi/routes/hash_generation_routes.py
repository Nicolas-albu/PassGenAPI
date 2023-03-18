from fastapi import APIRouter

from passgenapi.routes.models.hash_model import HashModel
from passgenapi.generator.hash_generator import HashGenerator

hash_routes = APIRouter()


@hash_routes.post("/hash/")
async def post_hash_generator(hash_definitions: HashModel) -> dict:
    """Router POST method to create a new hash with the passed parameters

    Args:
        hash_definitions (Hash): parameters for the new hash

    Returns:
        dict: the new hash generated in JSON format
    """
    return {
        "hash": HashGenerator(
            data_for_encrypt=hash_definitions.data_for_encrypt,
            hash_type=hash_definitions.hash_type,
        ).generate_hash()
    }
