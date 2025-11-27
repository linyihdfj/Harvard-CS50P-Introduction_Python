from twttr import shorten
def test_shorten_no_vowels():
    assert shorten("hll") == "hll"
def test_shorten_all_vowels():
    assert shorten("aeiouAEIOU") == ""
def test_shorten_mixed():
    assert shorten("Hello, World!") == "Hll, Wrld!"
def test_shorten_empty_string():
    assert shorten("") == ""
def test_shorten_with_numbers_and_symbols():
    assert shorten("Th1s 1s @ t3st!") == "Th1s 1s @ t3st!"
def test_shorten_only_symbols():
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"
def test_shorten_long_text():
    input_text = "This is a longer piece of text to test the shorten function."
    expected_output = "Ths s  lngr pc f txt t tst th shrtn fnctn."
    assert shorten(input_text) == expected_output