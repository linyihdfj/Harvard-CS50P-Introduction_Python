from plates import is_valid
def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO1") == True
    
def test_invalid_plates():
    assert is_valid("C") == False  # Too short
    assert is_valid("CS50P123") == False  # Too long
    assert is_valid("CS@50") == False  # Special character
    assert is_valid("50CS") == False  # Starts with a number
    assert is_valid("HELLO01") == False  # Leading zero in number
    assert is_valid("HELLO123") == False  # More than two numbers
    assert is_valid("CS50P") == False
    assert is_valid("A1B2C3") == False
    assert is_valid("PYTHON3") == False