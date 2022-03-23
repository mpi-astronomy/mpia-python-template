import pytest
import my_package.example

def test_type():
    """
    Test addition with float, int and strung.
    """
    assert my_package.example.add_one(1) == 2
    assert my_package.example.add_one(1.1) == 2.1
    assert my_package.example.add_one('1') == '11'

def test_error():
    """
    Test addition with list.
    """
    with pytest.raises(TypeError):
        my_package.example.add_one([1])
