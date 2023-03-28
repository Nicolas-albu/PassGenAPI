from hashlib import md5

import pytest

from passgenapi.generators.hash_generator import HashGenerator

"""@pytest.fixture
def hash_generator():
    return HashGenerator("test data", "md5")"""


def test_hashgenerator_initialization():
    # Testa se a instância é criada corretamente
    hg = HashGenerator("hello", "md5")
    assert isinstance(hg, HashGenerator)
    assert hg._HashGenerator__data_to_encrypt == b"hello"
    assert hg._HashGenerator__hash_type == "md5"


def test_hashgenerator_generate_hash():
    # Testa se o método generate_hash() retorna a hash correta para cada tipo de hash
    hg = HashGenerator("hello", "md5")
    assert hg.generate_hash() == "5d41402abc4b2a76b9719d911017c592"

    hg = HashGenerator("hello", "sha1")
    assert hg.generate_hash() == "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"

    hg = HashGenerator("hello", "sha224")
    assert (
        hg.generate_hash()
        == "ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193"
    )

    hg = HashGenerator("hello", "sha256")
    assert (
        hg.generate_hash()
        == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    )

    hg = HashGenerator("hello", "sha384")
    assert (
        hg.generate_hash()
        == "59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f"
    )


def test_hash_generator_generate_hash_invalid_type():
    hg = HashGenerator("hello", "r45")
    hg._HashGenerator__hash_type = "invalid hash type"
    with pytest.raises(TypeError):
        hg.generate_hash()


def test_hash_generator_str():
    hg = HashGenerator("testando", "md5")
    assert str(hg) == md5(b"testando").hexdigest()
