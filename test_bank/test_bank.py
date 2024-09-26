from bank import value

def main():
    test_value_hello()
    test_value_h()
    test_value_random()


def test_value_hello():
    assert value("Hello") == 0
    assert value("hello") == 0


def test_value_h():
    assert value("Hey") == 20
    assert value("hi") == 20


def test_value_random():
    assert value("What's up") == 100
    assert value("random") == 100
