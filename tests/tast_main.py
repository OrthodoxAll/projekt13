from src.main import divider

def test_devider():
    assert divider(2,1) == 6

    assert divider(2,0) == 0
