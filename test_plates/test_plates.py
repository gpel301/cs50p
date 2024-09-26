from plates import is_valid

def main():
    test_is_valid_punct()
    test_is_valid_length()
    test_is_valid_start()
    test_is_valid_order()

def test_is_valid_punct():
    assert is_valid("xx615.") == False
    assert is_valid("xx 615") == False

def test_is_valid_length():
    assert is_valid("x") == False
    assert is_valid("xxxx123") == False


def test_is_valid_start():
    assert is_valid("123xx") == False
    assert is_valid("x123") == False


def test_is_valid_order():
    assert is_valid("xxx012") == False
    assert is_valid("xxx12x") == False
