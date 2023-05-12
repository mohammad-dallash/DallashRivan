
from task2 import add

def test_empty_string():
    assert add("") == 0

def test_single_number():
    assert add("5") == 5

def test_two_numbers():
    assert add("2,1001") == 2



def test_newlines_between_numbers():
    assert add("1\n2,3") == 6

def test_support_different_delimiters():
    assert add("//;\n1;2") == 3

def test_negative_numbers():
    try:
        add("-1,2")
    except Exception as e:
        assert str(e) == "Sorry, no negative numbers allowed"
