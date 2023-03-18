from hashlib import md5, sha1, sha224, sha256, sha384, sha3_256


class HashGenerator:
    """Class for generator hashes"""

    def __init__(self, data_for_encrypt: str, hash_type: str):
        """Parameters to set the hash

        Args:
            data_for_encrypt (str): data to hash
            hash_type (str): type of hash that will be of the data
        """
        self.__data_to_encrypt: str = data_for_encrypt.encode()
        self.__hash_type: str = hash_type.lower()

    def generate_hash(self) -> str:
        """method that call the hash method to pass the data to hash

        Returns:
            str: hash generated
        """
        __hashes_generation_cases: dict[str, callable] = {
            "md5": md5,
            "sha1": sha1,
            "sha224": sha224,
            "sha256": sha256,
            "sha384": sha384,
            "sha3-256": sha3_256
        }
        __encrypted_data: str = __hashes_generation_cases.get(self.__hash_type, None)
        
        return __encrypted_data(self.__data_to_encrypt).hexdigest()

    def __str__(self) -> str:
        return self.generate_hash()