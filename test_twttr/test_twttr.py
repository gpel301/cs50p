from twttr import shorten

def main():
    test_shorten()
    # test_defult_shorten()
    # test_upper_shorten()
    # test_lower_shorten()
    # test_numbers_shorten()
    # test_punct_shorten()


def test_shorten():
    assert shorten("ThIsIsAtest") == "Thsstst"
    assert shorten("HELLO") == "HLL"
    assert shorten("happy") == "hppy"
    assert shorten("2113") == "2113"
    assert shorten("!.#") == "!.#"


# def test_defult_shorten():
#     assert shorten("ThIsIsAtest") == "Thsstst"


# def test_upper_shorten():
#     assert shorten("HELLO") == "HLL"


# def test_lower_shorten():
#     assert shorten("happy") == "hppy"


# def test_numbers_shorten():
#     assert shorten("2113") == "2113"


# def test_punct_shorten():
#     assert shorten("!.#") == "!.#"



