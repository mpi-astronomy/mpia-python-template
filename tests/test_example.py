import pytest

from my_package.example import add_one


def test_type():
    """
    Test addition with float, int and strung.
    """
    assert add_one(1) == 2
    assert add_one(1.1) == 2.1
    assert add_one('1') == '11'


def test_error():
    """
    Test addition with list.
    """
    with pytest.raises(TypeError):
        add_one([1])
