import pytest


def test_aaa():
    print("aaa")
    assert True


def test_bbb():
    print("bbbb")
    assert True


if __name__ == '__main__':
    pytest.main(["-vs", "--alluredir", "report/allure_report"])
