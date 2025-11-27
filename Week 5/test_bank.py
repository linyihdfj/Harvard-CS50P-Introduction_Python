from bank import value
def test_value_hello():
    assert value("hello") == "$0"
def test_value_h():
    assert value("hi") == "$20"
def test_value_other():
    assert value("goodbye") == "$100"