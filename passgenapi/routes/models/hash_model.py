"""This module contains the parameter template for the hash generation POST route."""

from pydantic import BaseModel


class HashModel(BaseModel):
    """JSON parameter model class to generate hash.

    Args:
        * BaseModel (pydantic.BaseModel): Hash template for the parameters of a JSON request from endpoint /hash/
        * data_for_encrypt (str): given that will be hashed
        * hash_type (str): Hash types, how sha1, sha224, sha256, sha384, sha3-256 and md5
    """

    data_for_encrypt: str
    hash_type: str
