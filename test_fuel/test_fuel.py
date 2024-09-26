from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_convert_error()
    test_gauge()

def test_convert():
    assert convert("99/100") == 99
    assert convert("1/2") == 50
    assert convert("1/100") == 1

def test_convert_error():
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
