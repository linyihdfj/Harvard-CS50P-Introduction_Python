from fuel import convert,gauge
from pytest import raises

def test_convert():
    assert convert("1/2") == 0.5
    assert convert("3/4") == 0.75
    assert convert("2/3") == (2/3)
    
    with raises(ZeroDivisionError):
        convert("3/0")
    
    with raises(ValueError):
        convert("5/4")
    
    with raises(ValueError):
        convert("abc")
def test_gauge():
    assert gauge(0.0) == "E"
    assert gauge(0.005) == "E"
    assert gauge(0.01) == "1%"
    assert gauge(0.5) == "50%"
    assert gauge(0.99) == "99%"
    assert gauge(1.0) == "F"
    assert gauge(1.005) == "F"