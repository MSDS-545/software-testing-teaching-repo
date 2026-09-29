from tdd_lab.starter.password_policy import is_valid_password


def test_password_with_eight_characters_digit_and_uppercase_is_valid():
    assert is_valid_password("Testing1") is True


def test_short_password_is_invalid():
    assert is_valid_password("Test1") is False
