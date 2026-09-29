from tdd_lab.solution.password_policy import is_valid_password


def test_valid_password():
    assert is_valid_password("Testing1") is True


def test_short_password():
    assert is_valid_password("Test1") is False


def test_password_requires_digit():
    assert is_valid_password("TestingX") is False


def test_password_requires_uppercase():
    assert is_valid_password("testing1") is False
