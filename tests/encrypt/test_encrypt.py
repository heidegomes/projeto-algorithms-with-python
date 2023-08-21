from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("string", "1")
    assert encrypt_message("string", 6) == "gnirts"
    assert encrypt_message("string", -2) == "gnirts"
    assert encrypt_message("string", 2) == "gnir_ts"
