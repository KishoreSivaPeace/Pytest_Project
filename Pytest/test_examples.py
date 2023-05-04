import pytest
from configreader import readconfig


def test_login_in():
    print("True")


def test_settings():
    print("Complete")


def get_data():
    return [
        ("KishoreSiva", "1103"),
        ("PeaceArt", "1103")
    ]


@pytest.mark.parametrize("username, password", get_data())
def test_check1(username, password):
    print(username, "--", password)


def get_data():
    return [
        ("KISHORESIVADB", "KishoreSiva", "1103"),
        ("KISHORESIVADB", "PeaceArt", "1103")
    ]


@pytest.mark.parametrize("DBname, username, password", get_data())
def test_check2(DBname, username, password):
    print(DBname, "--", username, "--", password)


def test_example():
    print(readconfig("URL", "live"))

