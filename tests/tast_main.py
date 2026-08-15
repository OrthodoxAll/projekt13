import pytest

from src.main import divider

def test_devider():
    assert divider(2,1) == 6

    assert divider(2,0) == 0


def test_reverse_strinf_numbers()
    assert reverse_strring('1234') == '4321'