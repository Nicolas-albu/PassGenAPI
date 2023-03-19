from passgenapi.generators.hash_generator import HashGenerator


def test_md5():
    generated_hash = HashGenerator("TEST", "md5").generate_hash()
    assert generated_hash is not None
    assert generated_hash == "033bd94b1168d7e4f0d644c3c95e35bf"
