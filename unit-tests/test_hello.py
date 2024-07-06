from hello import hello


def test_padrao():
    assert hello() == "Olá, mundo"


def test_termo():
    assert hello("David") == "Olá, David"
