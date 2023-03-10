from pydantic import BaseModel

class HashModel(BaseModel):
    """JSON parameter model class to generate hash
    
    Args:
        * BaseModel (pydantic.BaseModel): Hash template for the parameters of a JSON request from endpoint /password/
        * data_for_encrypt (str): given that will be hashed
        * hash_type (str): Hash types
    """
    data_for_encrypt: str
    hash_type: str